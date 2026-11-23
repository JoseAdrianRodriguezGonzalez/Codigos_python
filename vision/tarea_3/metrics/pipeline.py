import numpy as np
import pandas as pd

from metrics.rendimientos import measure_time
from metrics.memoria import measure_memory


def benchmark_detectors(
    names: list,
    images: list[np.ndarray],
    detectors: dict,
    repeats: int = 10,
    warmup: int = 2,
) -> pd.DataFrame:

    if len(names) != len(images):
        raise ValueError(
            "names and images must have the same length"
        )

    records = []

    for image_name, image in zip(names, images):

        height, width = image.shape
        pixels = height * width

        for name, detector in detectors.items():

            # -------------------------
            # Tiempo
            # -------------------------

            time_result = measure_time(
                detector,
                image,
                repeats=repeats,
                warmup=warmup,
            )

            # -------------------------
            # Memoria
            # -------------------------

            memory_result = measure_memory(
                detector,
                image,
            )

            # -------------------------
            # Registro
            # -------------------------

            records.append({
                "image": image_name,

                "operator": name,

                "width": width,
                "height": height,
                "pixels": pixels,

                "mean_ms": (
                    time_result["mean_ms"]
                ),

                "median_ms": (
                    time_result["median_ms"]
                ),

                "std_ms": (
                    time_result["std_ms"]
                ),

                "ms_per_pixel": (
                    time_result["ms_per_pixel"]
                ),

                "us_per_pixel": (
                    time_result["us_per_pixel"]
                ),

                "memory_current_mb": (
                    memory_result[
                        "memory_current_mb"
                    ]
                ),

                "memory_peak_mb": (
                    memory_result[
                        "memory_peak_mb"
                    ]
                ),
            })

    return pd.DataFrame(records)
