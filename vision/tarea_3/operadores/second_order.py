import numpy as np


def zero_crossing(laplacian: np.ndarray,threshold: float = 0.0,) :
    edges = np.zeros(
        laplacian.shape,
        dtype=np.uint8,
    )
    center = laplacian[1:-1, 1:-1]
    neighbors = [
        laplacian[:-2, 1:-1],
        laplacian[2:, 1:-1],
        laplacian[1:-1, :-2],
        laplacian[1:-1, 2:],
        laplacian[:-2, :-2],
        laplacian[:-2, 2:],
        laplacian[2:, :-2],
        laplacian[2:, 2:],
    ]
    positive = center > threshold
    negative = center < -threshold
    crossing = np.zeros_like(center, dtype=bool)
    for neighbor in neighbors:
        crossing |= (
            (positive & (neighbor < -threshold))
            | (negative & (neighbor > threshold))
        )
    edges[1:-1, 1:-1] = crossing * 255

    return edges
