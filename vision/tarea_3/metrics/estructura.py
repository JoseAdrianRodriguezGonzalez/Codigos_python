import cv2
import numpy as np


# ============================================================
# Utilidades
# ============================================================

def binary_mask(
    image: np.ndarray,
) -> np.ndarray:
    """
    Converts an edge map into a boolean binary mask.
    """

    return image > 0


def edge_density(
    edges: np.ndarray,
) -> float:
    """
    Calculates the proportion of edge pixels
    in an image.

    Returns
    -------
    float
        Value between 0 and 1.
    """

    edges = binary_mask(edges)

    return float(
        np.count_nonzero(edges)
        / edges.size
    )


# ============================================================
# Esquinas
# ============================================================

def detect_corners(
    edges: np.ndarray,
    max_corners: int = 100,
    quality_level: float = 0.01,
    min_distance: float = 5.0,
) -> np.ndarray:
    """
    Detects corners in an edge map.

    Parameters
    ----------
    edges:
        Binary edge map.

    max_corners:
        Maximum number of corners.

    quality_level:
        Minimum accepted corner quality.

    min_distance:
        Minimum distance between corners.

    Returns
    -------
    np.ndarray
        Array with shape (N, 2), where each row
        contains (x, y).
    """

    image = edges.astype(np.uint8)

    corners = cv2.goodFeaturesToTrack(
        image,
        maxCorners=max_corners,
        qualityLevel=quality_level,
        minDistance=min_distance,
    )

    if corners is None:
        return np.empty(
            (0, 2),
            dtype=np.float32,
        )

    return corners.reshape(
        -1,
        2,
    )


def match_points(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 2.0,
) -> tuple[int, int, int]:
    """
    Matches detected points against reference points.

    A detected point is considered a true positive
    when it is within the specified tolerance.

    Returns
    -------
    tuple[int, int, int]
        TP, FP, FN
    """

    detected = np.asarray(
        detected,
        dtype=np.float32,
    )

    reference = np.asarray(
        reference,
        dtype=np.float32,
    )

    if len(detected) == 0:
        return 0, 0, len(reference)

    if len(reference) == 0:
        return 0, len(detected), 0

    matched_reference = set()
    true_positive = 0

    for point in detected:

        distances = np.linalg.norm(
            reference - point,
            axis=1,
        )

        nearest = np.argmin(distances)
        distance = distances[nearest]

        if (
            distance <= tolerance
            and nearest not in matched_reference
        ):
            true_positive += 1
            matched_reference.add(nearest)

    false_positive = (
        len(detected)
        - true_positive
    )

    false_negative = (
        len(reference)
        - true_positive
    )

    return (
        true_positive,
        false_positive,
        false_negative,
    )


def corner_metrics(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 2.0,
) -> dict:
    """
    Calculates precision, recall and F1
    for detected corners.
    """

    tp, fp, fn = match_points(
        detected,
        reference,
        tolerance=tolerance,
    )

    precision = (
        tp / (tp + fp)
        if tp + fp > 0
        else 0.0
    )

    recall = (
        tp / (tp + fn)
        if tp + fn > 0
        else 0.0
    )

    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = (
            2
            * precision
            * recall
            / (precision + recall)
        )

    return {
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


# ============================================================
# Líneas y curvas
# ============================================================

def structure_recall(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 1.5,
) -> float:
    """
    Calculates the proportion of reference structure
    that has a detected edge within the specified
    spatial tolerance.

    Useful for evaluating lines and curves.
    """

    detected = binary_mask(detected)
    reference = binary_mask(reference)

    if not np.any(reference):
        return 0.0

    distance = cv2.distanceTransform(
        (~detected).astype(np.uint8),
        cv2.DIST_L2,
        3,
    )

    matched = (
        distance[reference]
        <= tolerance
    )

    return float(
        np.mean(matched)
    )


def structure_precision(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 1.5,
) -> float:
    """
    Calculates the proportion of detected structure
    that is spatially supported by the reference.
    """

    detected = binary_mask(detected)
    reference = binary_mask(reference)

    if not np.any(detected):
        return 0.0

    distance = cv2.distanceTransform(
        (~reference).astype(np.uint8),
        cv2.DIST_L2,
        3,
    )

    matched = (
        distance[detected]
        <= tolerance
    )

    return float(
        np.mean(matched)
    )


def structure_f1(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 1.5,
) -> float:
    """
    Calculates F1 for spatial structure preservation.
    """

    precision = structure_precision(
        detected,
        reference,
        tolerance=tolerance,
    )

    recall = structure_recall(
        detected,
        reference,
        tolerance=tolerance,
    )

    if precision + recall == 0:
        return 0.0

    return float(
        2
        * precision
        * recall
        / (precision + recall)
    )


# ============================================================
# Contornos cerrados
# ============================================================

def count_connected_components(
    edges: np.ndarray,
) -> int:
    """
    Counts connected components in a binary edge map.
    """

    binary = (
        binary_mask(edges)
        .astype(np.uint8)
    )

    num_labels, _ = (
        cv2.connectedComponents(
            binary,
            connectivity=8,
        )
    )

    return num_labels - 1


def contour_closure(
    edges: np.ndarray,
) -> dict:
    """
    Estimates contour closure using connected contours.

    Returns the number of contours and the number
    of contours that are closed according to OpenCV.
    """

    binary = (
        binary_mask(edges)
        .astype(np.uint8)
        * 255
    )

    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    total = len(contours)

    if total == 0:
        return {
            "total_contours": 0,
            "closed_contours": 0,
            "closure_rate": 0.0,
        }

    closed = 0

    for contour in contours:

        if len(contour) < 3:
            continue

        perimeter = cv2.arcLength(
            contour,
            closed=True,
        )

        if perimeter <= 0:
            continue

        closed += 1

    return {
        "total_contours": total,
        "closed_contours": closed,
        "closure_rate": (
            closed / total
        ),
    }


# ============================================================
# Detalle fino
# ============================================================

def detail_recall(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 1.5,
) -> float:
    """
    Measures how much fine structure from the reference
    is preserved by the detector.

    This is essentially spatial recall and is useful
    when reference represents fine structures.
    """

    return structure_recall(
        detected,
        reference,
        tolerance=tolerance,
    )


# ============================================================
# Evaluación conjunta de estructura
# ============================================================

def evaluate_structure(
    detected: np.ndarray,
    reference: np.ndarray,
    tolerance: float = 1.5,
) -> dict:
    """
    Calculates the general structural metrics
    for a detected edge map.

    Parameters
    ----------
    detected:
        Detected edge map.

    reference:
        Reference edge map.

    tolerance:
        Maximum spatial distance in pixels
        for considering a structure preserved.

    Returns
    -------
    dict
        Structural metrics.
    """

    structure_precision_value = (
        structure_precision(
            detected,
            reference,
            tolerance=tolerance,
        )
    )

    structure_recall_value = (
        structure_recall(
            detected,
            reference,
            tolerance=tolerance,
        )
    )

    structure_f1_value = (
        structure_f1(
            detected,
            reference,
            tolerance=tolerance,
        )
    )

    contour_result = contour_closure(
        detected
    )

    return {
        "edge_density": edge_density(
            detected
        ),

        "structure_precision": (
            structure_precision_value
        ),

        "structure_recall": (
            structure_recall_value
        ),

        "structure_f1": (
            structure_f1_value
        ),

        "connected_components": (
            count_connected_components(
                detected
            )
        ),

        "total_contours": (
            contour_result[
                "total_contours"
            ]
        ),

        "closed_contours": (
            contour_result[
                "closed_contours"
            ]
        ),

        "closure_rate": (
            contour_result[
                "closure_rate"
            ]
        ),
    }
