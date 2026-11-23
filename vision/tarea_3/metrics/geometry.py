import cv2
import numpy as np


def measure_edge_width(
    profile: np.ndarray,
    threshold: float = 0,
) -> float:
    """
    Measures the width of a detected edge in a 1D profile.

    Parameters
    ----------
    profile:
        One-dimensional edge response/profile.

    threshold:
        Minimum response considered part of the edge.

    Returns
    -------
    float
        Width of the detected region in pixels.
    """

    profile = np.asarray(
        profile,
        dtype=np.float32,
    )

    mask = profile > threshold

    if not np.any(mask):
        return 0.0

    indices = np.where(mask)[0]

    return float(
        indices[-1] - indices[0] + 1
    )


def count_connected_components(
    edges: np.ndarray,
) -> int:
    """
    Counts connected components in a binary edge map.
    """

    binary = (
        edges > 0
    ).astype(np.uint8)

    num_labels, _ = cv2.connectedComponents(
        binary,
        connectivity=8,
    )

    return num_labels - 1


def distance_to_reference(
    source: np.ndarray,
    reference: np.ndarray,
) -> np.ndarray:
    """
    Computes the distance from every pixel in source
    to the nearest pixel belonging to reference.
    """

    source = source > 0
    reference = reference > 0

    if not np.any(reference):
        raise ValueError(
            "Reference contains no edge pixels."
        )

    reference_uint8 = (
        reference.astype(np.uint8)
    )

    distance = cv2.distanceTransform(
        1 - reference_uint8,
        cv2.DIST_L2,
        3,
    )

    return distance[source]


def localization_error(
    detected: np.ndarray,
    reference: np.ndarray,
) -> float:
    """
    Mean localization error from detected edges
    to the reference edges.
    """

    detected = detected > 0
    reference = reference > 0

    if not np.any(detected):
        return float("inf")

    if not np.any(reference):
        return float("inf")

    errors = distance_to_reference(
        detected,
        reference,
    )

    return float(
        errors.mean()
    )


def symmetric_localization_error(
    detected: np.ndarray,
    reference: np.ndarray,
) -> float:
    """
    Symmetric mean localization error.

    Measures both:
        detected -> reference
        reference -> detected
    """

    detected = detected > 0
    reference = reference > 0

    if not np.any(detected):
        return float("inf")

    if not np.any(reference):
        return float("inf")

    detected_to_reference = (
        distance_to_reference(
            detected,
            reference,
        ).mean()
    )

    reference_to_detected = (
        distance_to_reference(
            reference,
            detected,
        ).mean()
    )

    return float(
        (
            detected_to_reference
            + reference_to_detected
        ) / 2
    )
