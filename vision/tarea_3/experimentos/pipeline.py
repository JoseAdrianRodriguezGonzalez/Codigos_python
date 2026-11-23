
from operadores.detect_edges import pipeline_detectors
def run_dataset(
    names,
    images,
    threshold=50,
):
    if len(names) != len(images):
        raise ValueError(
            "names and images must have the same length"
        )

    results = {}

    for name, image in zip(names, images):

        results[name] = pipeline_detectors(
            image,
            threshold,
        )

    return results
