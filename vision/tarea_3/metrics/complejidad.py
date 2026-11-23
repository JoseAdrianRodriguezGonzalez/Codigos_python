import numpy as np
import pandas as pd

from metrics.rendimiento import measure_time


def benchmark_scalability(
    images: dict,
    detectors: dict,
    repeats: int = 5,
) -> pd.DataFrame:

    records = []

    for resolution, image in images.items():

        height, width = image.shape
        pixels = height * width

        for name, detector in detectors.items():

            result = measure_time(
                detector,
                image,
                repeats=repeats,
            )

            records.append({
                "resolution": resolution,
                "width": width,
                "height": height,
                "pixels": pixels,
                "operator": name,
                "mean_ms": result["mean_ms"],
                "median_ms": result["median_ms"],
                "std_ms": result["std_ms"],
                "ms_per_pixel": result["ms_per_pixel"],
                "us_per_pixel": result["us_per_pixel"],
            })

    return pd.DataFrame(records)
