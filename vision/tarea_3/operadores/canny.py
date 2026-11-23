import cv2
import numpy as np

from collections import deque


def gaussian_smoothing(image,sigma):
    return cv2.GaussianBlur(
        image,
        ksize=(0, 0),
        sigmaX=sigma,
        sigmaY=sigma,
    )


def calculate_gradient(
    image: np.ndarray,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:

    gx = cv2.Sobel(
        image,
        cv2.CV_32F,
        1,
        0,
        ksize=3,
    )

    gy = cv2.Sobel(
        image,
        cv2.CV_32F,
        0,
        1,
        ksize=3,
    )

    magnitude = np.sqrt(
        gx**2 + gy**2
    )

    direction = np.arctan2(
        gy,
        gx,
    )

    return gx, gy, magnitude, direction
def non_maximum_suppression(
    magnitude: np.ndarray,
    direction: np.ndarray,
) -> np.ndarray:

    angle = np.rad2deg(direction)
    angle[angle < 0] += 180

    result = np.zeros_like(
        magnitude,
        dtype=np.float32,
    )

    for i in range(1, magnitude.shape[0] - 1):
        for j in range(1, magnitude.shape[1] - 1):

            current_angle = angle[i, j]
            current = magnitude[i, j]

            if (
                0 <= current_angle < 22.5
                or 157.5 <= current_angle <= 180
            ):
                n1 = magnitude[i, j + 1]
                n2 = magnitude[i, j - 1]

            elif 22.5 <= current_angle < 67.5:
                n1 = magnitude[i - 1, j + 1]
                n2 = magnitude[i + 1, j - 1]

            elif 67.5 <= current_angle < 112.5:
                n1 = magnitude[i - 1, j]
                n2 = magnitude[i + 1, j]

            else:
                n1 = magnitude[i - 1, j - 1]
                n2 = magnitude[i + 1, j + 1]

            if current >= n1 and current >= n2:
                result[i, j] = current

    return result
def double_threshold(
    magnitude: np.ndarray,
    tlow: float,
    thigh: float,
) -> np.ndarray:

    strong = 255
    weak = 75

    result = np.zeros_like(
        magnitude,
        dtype=np.uint8,
    )

    result[magnitude >= thigh] = strong

    result[
        (magnitude >= tlow)
        & (magnitude < thigh)
    ] = weak

    return result
def hysteresis(
    thresholded: np.ndarray,
) -> np.ndarray:

    strong = 255
    weak = 75

    result = thresholded.copy()

    queue = deque(
        zip(
            *np.where(
                result == strong
            )
        )
    )

    height, width = result.shape

    while queue:

        i, j = queue.popleft()

        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):

                if di == 0 and dj == 0:
                    continue

                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < height
                    and 0 <= nj < width
                    and result[ni, nj] == weak
                ):
                    result[ni, nj] = strong
                    queue.append((ni, nj))

    result[result != strong] = 0

    return result
def canny(
    image: np.ndarray,
    sigma: float,
    tlow: float,
    thigh: float,
) -> dict:

    blurred = gaussian_smoothing(
        image,
        sigma,
    )

    gx, gy, magnitude, direction = (
        calculate_gradient(blurred)
    )

    suppressed = non_maximum_suppression(
        magnitude,
        direction,
    )

    thresholded = double_threshold(
        suppressed,
        tlow,
        thigh,
    )

    edges = hysteresis(
        thresholded,
    )

    return {
        "blurred": blurred,
        "gx": gx,
        "gy": gy,
        "magnitude": magnitude,
        "direction": direction,
        "suppressed": suppressed,
        "thresholded": thresholded,
        "edges": edges,
    }
