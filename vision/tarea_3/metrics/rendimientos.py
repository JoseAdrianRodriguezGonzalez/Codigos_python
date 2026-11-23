import time
import numpy as np


def measure_time(
    detector,
    image: np.ndarray,
    repeats: int = 10,
    warmup: int = 2,
) -> dict:

    # -------------------------
    # Warm-up
    # -------------------------

    for _ in range(warmup):
        detector(image)

    # -------------------------
    # Medición
    # -------------------------

    times = []

    for _ in range(repeats):

        start = time.perf_counter()

        detector(image)

        end = time.perf_counter()

        times.append(
            end - start
        )

    times = np.asarray(times)

    height, width = image.shape
    pixels = height * width

    mean_ms = times.mean() * 1000
    median_ms = np.median(times) * 1000
    std_ms = times.std() * 1000

    return {
        "mean_ms": mean_ms,
        "median_ms": median_ms,
        "std_ms": std_ms,
        "pixels": pixels,
        "ms_per_pixel": (
            mean_ms / pixels
        ),
        "us_per_pixel": (
            mean_ms * 1000 / pixels
        ),
    }
