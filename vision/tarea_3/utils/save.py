
from pathlib import Path
import pandas as pd


def save_results(
    synthetic_results,
    bsds_results,
    synthetic_benchmark,
    bsds_benchmark,
    output_dir="results",
):
    """
    Guarda los resultados de evaluación y benchmark.

    Parameters
    ----------
    synthetic_results : pandas.DataFrame
        Métricas obtenidas sobre el dataset sintético.

    bsds_results : pandas.DataFrame
        Métricas obtenidas sobre BSDS.

    synthetic_benchmark : pandas.DataFrame
        Benchmark computacional sobre el dataset sintético.

    bsds_benchmark : pandas.DataFrame
        Benchmark computacional sobre BSDS.

    output_dir : str or Path
        Directorio raíz donde se almacenarán los resultados.
    """

    output_dir = Path(output_dir)

    synthetic_dir = output_dir / "synthetic"
    bsds_dir = output_dir / "bsds"

    synthetic_dir.mkdir(parents=True, exist_ok=True)
    bsds_dir.mkdir(parents=True, exist_ok=True)

    # ==========================================
    # Synthetic dataset
    # ==========================================

    synthetic_results.to_csv(
        synthetic_dir / "metrics.csv",
        index=False,
    )

    synthetic_benchmark.to_csv(
        synthetic_dir / "benchmark.csv",
        index=False,
    )

    # ==========================================
    # BSDS
    # ==========================================

    bsds_results.to_csv(
        bsds_dir / "metrics.csv",
        index=False,
    )

    bsds_benchmark.to_csv(
        bsds_dir / "benchmark.csv",
        index=False,
    )

    print(f"Resultados guardados en: {output_dir}")
import numpy as np



import pandas as pd

from metrics.calidad import calculate_entropy
from metrics.geometry import localization_error
from metrics.estructura import evaluate_structure


def evaluate_dataset(
    results: dict,
    ground_truth: dict,
) -> pd.DataFrame:

    records = []

    for image_name, operators in results.items():

        if image_name not in ground_truth:
            raise KeyError(
                f"No existe ground truth para: {image_name}"
            )

        reference = ground_truth[image_name]

        for operator_name, result in operators.items():

            # ==================================================
            # Detector sin parámetros
            # ==================================================

            if "edges" in result:

                edges = result["edges"]

                structure = evaluate_structure(
                    edges,
                    reference,
                )

                records.append({
                    "image": image_name,
                    "operator": operator_name,
                    "parameter": "default",

                    "entropy": calculate_entropy(
                        edges
                    ),

                    "localization_error": (
                        localization_error(
                            edges,
                            reference,
                        )
                    ),

                    **structure,
                })

            # ==================================================
            # Detector con parámetros
            # ==================================================

            else:

                for parameter, parameter_result in result.items():

                    if "edges" not in parameter_result:
                        continue

                    edges = parameter_result["edges"]

                    structure = evaluate_structure(
                        edges,
                        reference,
                    )

                    records.append({
                        "image": image_name,
                        "operator": operator_name,
                        "parameter": parameter,

                        "entropy": calculate_entropy(
                            edges
                        ),

                        "localization_error": (
                            localization_error(
                                edges,
                                reference,
                            )
                        ),

                        **structure,
                    })

    return pd.DataFrame(records)
