from preparacion.pipeline import preparacion_pipeline
import argparse
from experimentos.pipeline import run_dataset
from metrics.pipeline import benchmark_detectors
from operadores.configuracion import  BENCHMARK_DETECTORS
from utils.save import save_results,evaluate_dataset
def main():
    parser=argparse.ArgumentParser(description="Vision project")
    parser.add_argument("--generate",action="store_true",help="Genera el dataset")
    parser.add_argument("--plots",action="store_true",help="Muestra los plots")
    args=parser.parse_args()
    
    data = preparacion_pipeline(args)
    synthetic_results = run_dataset(
        data["synthetic"]["names"],
        data["synthetic"]["images"],
        threshold=50,
    )

    bsds_results = run_dataset(
        data["bsds"]["names"],
        data["bsds"]["images"],
        threshold=50,
    )
    print("RESULTADOS:")
    print(synthetic_results.keys())

    print("GROUND TRUTH:")
    print(data["synthetic"]["ground_truth"].keys())

    # ==========================================
    # Benchmark
    # ==========================================

    synthetic_metrics = evaluate_dataset(
        synthetic_results,
        data["synthetic"]["ground_truth"],
    )

    bsds_metrics = evaluate_dataset(
        bsds_results,
        data["bsds"]["ground_truth"],
    )
    print("\n=== ESTRUCTURA DERICHE ===")

    image_name = data["bsds"]["names"][0]

    print("Imagen:", image_name)

    print(
    "Parámetros:",
    bsds_results[image_name]["deriche"].keys()
    )

    for alpha, result in bsds_results[image_name]["deriche"].items():

        print(
            "alpha:",
            alpha,
            "| tipo:",
            type(result),
            "| keys:",
            result.keys() if isinstance(result, dict) else None,
        )
    synthetic_benchmark = benchmark_detectors(
    data["synthetic"]["names"],
    data["synthetic"]["images"],
    BENCHMARK_DETECTORS,
    )

    bsds_benchmark = benchmark_detectors(
    data["bsds"]["names"],
    data["bsds"]["images"],
    BENCHMARK_DETECTORS,
    )
    save_results(
        synthetic_metrics,
        bsds_metrics,
        synthetic_benchmark,
        bsds_benchmark,
    )
if __name__=="__main__":
    main()
