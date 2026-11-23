import tracemalloc
import numpy as np


def measure_memory(
    detector,
    image: np.ndarray,
) -> dict:

    tracemalloc.start()

    detector(image)

    current, peak = (
        tracemalloc.get_traced_memory()
    )

    tracemalloc.stop()

    return {
        "memory_current_mb": (
            current / (1024 ** 2)
        ),
        "memory_peak_mb": (
            peak / (1024 ** 2)
        ),
    }
import os
import psutil


def measure_rss(
    detector,
    image: np.ndarray,
) -> dict:

    process = psutil.Process(
        os.getpid()
    )

    before = process.memory_info().rss

    detector(image)

    after = process.memory_info().rss

    return {
        "rss_before_mb": (
            before / (1024 ** 2)
        ),
        "rss_after_mb": (
            after / (1024 ** 2)
        ),
        "rss_delta_mb": (
            (after - before)
            / (1024 ** 2)
        ),
    }
