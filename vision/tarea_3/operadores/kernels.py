import numpy as np


ROBERTS_X = np.array(
    [
        [1, 0],
        [0, -1],
    ],
    dtype=np.float32,
)

ROBERTS_Y = np.array(
    [
        [0, 1],
        [-1, 0],
    ],
    dtype=np.float32,
)


PREWITT_X = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ],
    dtype=np.float32,
)

PREWITT_Y = np.array(
    [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ],
    dtype=np.float32,
)


SOBEL_X = np.array(
    [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ],
    dtype=np.float32,
)

SOBEL_Y = np.array(
    [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ],
    dtype=np.float32,
)


SCHARR_X = np.array(
    [
        [-3, 0, 3],
        [-10, 0, 10],
        [-3, 0, 3],
    ],
    dtype=np.float32,
)

SCHARR_Y = np.array(
    [
        [-3, -10, -3],
        [0, 0, 0],
        [3, 10, 3],
    ],
    dtype=np.float32,
)
LAPLACIAN_KERNEL = np.array(
    [
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0],
    ],
    dtype=np.float32,
)
