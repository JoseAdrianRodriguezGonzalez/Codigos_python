import numpy as np


def calculate_mse(
    image: np.ndarray,
    reference: np.ndarray,
) -> float:

    image = image.astype(np.float32)
    reference = reference.astype(np.float32)

    if image.shape != reference.shape:
        raise ValueError(
            "Images must have the same shape."
        )

    mse = np.mean(
        (image - reference) ** 2
    )

    return float(mse)


def calculate_psnr(
    image: np.ndarray,
    reference: np.ndarray,
    max_value: float = 255.0,
) -> float:

    mse = calculate_mse(
        image,
        reference,
    )

    if mse == 0:
        return float("inf")

    return float(
        10 * np.log10(
            (max_value ** 2) / mse
        )
    )
import numpy as np


def calculate_entropy(
    image: np.ndarray,
) -> float:

    values, counts = np.unique(
        image,
        return_counts=True,
    )

    probabilities = (
        counts / counts.sum()
    )

    entropy = -np.sum(
        probabilities
        * np.log2(probabilities)
    )

    return float(entropy)
def degradation_rate(
    clean_score: float,
    noisy_score: float,
) -> float:

    if clean_score == 0:
        return 0.0

    return (
        (clean_score - noisy_score)
        / clean_score
    )
def coefficient_variation(
    values: np.ndarray,
) -> float:

    values = np.asarray(
        values,
        dtype=np.float32,
    )

    mean = values.mean()

    if mean == 0:
        return 0.0

    return float(
        values.std() / mean
    )
