from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURACIÓN
# ============================================================

RESULTS_DIR = Path("results")
REPORT_DIR = RESULTS_DIR / "report"

TABLES_DIR = REPORT_DIR / "tables"
FIGURES_DIR = REPORT_DIR / "figures"

DATASETS = {
    "synthetic": "Synthetic",
    "bsds": "BSDS500",
}

OPERATOR_ORDER = [
    "Roberts",
    "Prewitt",
    "Sobel",
    "Scharr",
    "Laplacian",
    "LoG",
    "Canny",
    "Deriche",
]


# ============================================================
# UTILIDADES
# ============================================================

def prepare_directories():
    """
    Crea los directorios necesarios para tablas y figuras.
    """

    TABLES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


def order_operators(df):
    """
    Ordena los operadores de acuerdo con OPERATOR_ORDER.
    """

    order = {
        name: index
        for index, name in enumerate(OPERATOR_ORDER)
    }

    df = df.copy()

    df["_operator_order"] = (
        df["operator"]
        .map(order)
        .fillna(len(order))
    )

    df = (
        df.sort_values("_operator_order")
        .drop(columns="_operator_order")
        .reset_index(drop=True)
    )

    return df


def mean_std(
    dataframe,
    group_columns,
    value_column,
):
    """
    Calcula media y desviación estándar.
    """

    result = (
        dataframe
        .groupby(
            group_columns,
            sort=False,
        )[value_column]
        .agg(
            mean="mean",
            std="std",
        )
        .reset_index()
    )

    return result


def format_mean_std(
    mean,
    std,
    decimals=3,
):
    """
    Formatea un valor como media ± desviación estándar.
    """

    if pd.isna(std):
        std = 0.0

    return (
        f"{mean:.{decimals}f} "
        f"$\\pm$ "
        f"{std:.{decimals}f}"
    )


def save_latex(
    dataframe,
    filename,
    caption=None,
    label=None,
):
    """
    Guarda un DataFrame como tabla LaTeX.
    """

    path = TABLES_DIR / filename

    latex = dataframe.to_latex(
        index=False,
        escape=False,
    )

    if caption is not None:
        latex = (
            "\\begin{table}[htbp]\n"
            "\\centering\n"
            f"{latex}\n"
            f"\\caption{{{caption}}}\n"
        )

        if label is not None:
            latex += (
                f"\\label{{{label}}}\n"
            )

        latex += "\\end{table}\n"

    path.write_text(
        latex,
        encoding="utf-8",
    )

    return path


def save_figure(
    filename,
    dpi=300,
):
    pdf_path = FIGURES_DIR / f"{filename}.pdf"
    png_path = FIGURES_DIR / f"{filename}.png"

    plt.savefig(
        pdf_path,
        bbox_inches="tight",
    )

    plt.savefig(
        png_path,
        dpi=dpi,
        bbox_inches="tight",
    )

    plt.close()

    return pdf_path, png_path
# ============================================================
# CARGA DE RESULTADOS
# ============================================================

def load_results(dataset):
    """
    Carga metrics.csv y benchmark.csv.
    """

    dataset_dir = RESULTS_DIR / dataset

    metrics_path = (
        dataset_dir / "metrics.csv"
    )

    benchmark_path = (
        dataset_dir / "benchmark.csv"
    )

    if not metrics_path.exists():
        raise FileNotFoundError(
            f"No existe: {metrics_path}"
        )

    if not benchmark_path.exists():
        raise FileNotFoundError(
            f"No existe: {benchmark_path}"
        )

    metrics = pd.read_csv(
        metrics_path
    )

    benchmark = pd.read_csv(
        benchmark_path
    )

    return metrics, benchmark


# ============================================================
# TABLA DE BENCHMARK
# ============================================================

def create_benchmark_table(
    benchmark,
    dataset,
):
    """
    Genera una tabla resumen de rendimiento.

    La media se calcula sobre las imágenes.
    """

    summary = (
        benchmark
        .groupby(
            "operator",
            sort=False,
        )
        .agg(
            mean_ms_mean=(
                "mean_ms",
                "mean",
            ),

            mean_ms_std=(
                "mean_ms",
                "std",
            ),

            median_ms_mean=(
                "median_ms",
                "mean",
            ),

            us_per_pixel_mean=(
                "us_per_pixel",
                "mean",
            ),

            us_per_pixel_std=(
                "us_per_pixel",
                "std",
            ),

            memory_peak_mean=(
                "memory_peak_mb",
                "mean",
            ),

            memory_peak_std=(
                "memory_peak_mb",
                "std",
            ),
        )
        .reset_index()
    )

    summary = order_operators(
        summary
    )

    table = pd.DataFrame()

    table["Operador"] = (
        summary["operator"]
    )

    table["Tiempo (ms)"] = [
        format_mean_std(
            mean,
            std,
            decimals=3,
        )
        for mean, std in zip(
            summary["mean_ms_mean"],
            summary["mean_ms_std"],
        )
    ]

    table["Mediana (ms)"] = (
        summary["median_ms_mean"]
        .map(lambda x: f"{x:.3f}")
    )

    table["$\mu$s/pixel"] = [
        format_mean_std(
            mean,
            std,
            decimals=5,
        )
        for mean, std in zip(
            summary["us_per_pixel_mean"],
            summary["us_per_pixel_std"],
        )
    ]

    table["Memoria pico (MB)"] = [
        format_mean_std(
            mean,
            std,
            decimals=3,
        )
        for mean, std in zip(
            summary["memory_peak_mean"],
            summary["memory_peak_std"],
        )
    ]

    save_latex(
        table,
        f"{dataset}_benchmark.tex",
        caption=(
            f"Rendimiento computacional de los "
            f"detectores sobre el conjunto {DATASETS[dataset]}."
        ),
        label=(
            f"tab:{dataset}_benchmark"
        ),
    )

    return summary


# ============================================================
# TABLA DE MÉTRICAS
# ============================================================

def create_metrics_table(
    metrics,
    dataset,
):
    """
    Genera una tabla con las métricas de calidad.

    Para operadores parametrizados se conserva
    cada parámetro individual.
    """

    group_columns = [
        "operator",
        "parameter",
    ]

    aggregations = {
        "entropy": [
            "mean",
            "std",
        ],

        "localization_error": [
            "mean",
            "std",
        ],

        "structure_precision": [
            "mean",
            "std",
        ],

        "structure_recall": [
            "mean",
            "std",
        ],

        "structure_f1": [
            "mean",
            "std",
        ],

        "edge_density": [
            "mean",
            "std",
        ],

        "connected_components": [
            "mean",
            "std",
        ],
    }

    summary = (
        metrics
        .groupby(
            group_columns,
            sort=False,
        )
        .agg(aggregations)
    )

    summary.columns = [
        f"{column}_{stat}"
        for column, stat in summary.columns
    ]

    summary = (
        summary
        .reset_index()
    )

    summary = order_operators(
        summary
    )

    table = pd.DataFrame()

    table["Operador"] = (
        summary["operator"]
    )

    table["Parámetro"] = (
        summary["parameter"]
    )

    table["Precisión"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            summary[
                "structure_precision_mean"
            ],
            summary[
                "structure_precision_std"
            ],
        )
    ]

    table["Recall"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            summary[
                "structure_recall_mean"
            ],
            summary[
                "structure_recall_std"
            ],
        )
    ]

    table["F1"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            summary[
                "structure_f1_mean"
            ],
            summary[
                "structure_f1_std"
            ],
        )
    ]

    table["Error localización"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            summary[
                "localization_error_mean"
            ],
            summary[
                "localization_error_std"
            ],
        )
    ]

    table["Entropía"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            summary[
                "entropy_mean"
            ],
            summary[
                "entropy_std"
            ],
        )
    ]

    table["Densidad"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            summary[
                "edge_density_mean"
            ],
            summary[
                "edge_density_std"
            ],
        )
    ]

    save_latex(
        table,
        f"{dataset}_metrics.tex",
        caption=(
            f"Métricas de calidad de los detectores "
            f"para el conjunto {DATASETS[dataset]}."
        ),
        label=(
            f"tab:{dataset}_metrics"
        ),
    )

    return summary


# ============================================================
# MEJOR CONFIGURACIÓN
# ============================================================

def create_best_f1_table(
    metrics,
    dataset,
):
    """
    Obtiene la configuración con mayor F1 promedio
    para cada operador.
    """

    summary = (
        metrics
        .groupby(
            [
                "operator",
                "parameter",
            ],
            sort=False,
        )
        .agg(
            f1_mean=(
                "structure_f1",
                "mean",
            ),

            f1_std=(
                "structure_f1",
                "std",
            ),

            precision_mean=(
                "structure_precision",
                "mean",
            ),

            recall_mean=(
                "structure_recall",
                "mean",
            ),

            localization_mean=(
                "localization_error",
                "mean",
            ),
        )
        .reset_index()
    )

    best_indices = (
        summary
        .groupby("operator")[
            "f1_mean"
        ]
        .idxmax()
    )

    best = (
        summary
        .loc[best_indices]
        .reset_index(drop=True)
    )

    best = order_operators(
        best
    )

    table = pd.DataFrame()

    table["Operador"] = (
        best["operator"]
    )

    table["Parámetro"] = (
        best["parameter"]
    )

    table["F1"] = [
        format_mean_std(
            mean,
            std,
        )
        for mean, std in zip(
            best["f1_mean"],
            best["f1_std"],
        )
    ]

    table["Precisión"] = (
        best["precision_mean"]
        .map(lambda x: f"{x:.3f}")
    )

    table["Recall"] = (
        best["recall_mean"]
        .map(lambda x: f"{x:.3f}")
    )

    table["Error localización"] = (
        best["localization_mean"]
        .map(lambda x: f"{x:.3f}")
    )

    save_latex(
        table,
        f"{dataset}_best_f1.tex",
        caption=(
            f"Mejor configuración de cada operador "
            f"según F1 promedio en {DATASETS[dataset]}."
        ),
        label=(
            f"tab:{dataset}_best_f1"
        ),
    )

    return best


# ============================================================
# GRÁFICA: TIEMPO
# ============================================================

def plot_runtime(
    benchmark,
    dataset,
):
    """
    Gráfica del tiempo promedio de ejecución.
    """

    summary = (
        benchmark
        .groupby("operator")
        .agg(
            mean=(
                "mean_ms",
                "mean",
            ),

            std=(
                "mean_ms",
                "std",
            ),
        )
        .reset_index()
    )

    summary = order_operators(
        summary
    )

    plt.figure(
        figsize=(10, 6)
    )

    x = np.arange(
        len(summary)
    )

    plt.bar(
        x,
        summary["mean"],
        yerr=summary["std"],
        capsize=4,
    )

    plt.xticks(
        x,
        summary["operator"],
        rotation=35,
        ha="right",
    )

    plt.ylabel(
        "Tiempo de ejecución (ms)"
    )

    plt.xlabel(
        "Operador"
    )

    plt.title(
        f"Tiempo de ejecución — {DATASETS[dataset]}"
    )

    plt.yscale("log")

    plt.grid(
        axis="y",
        alpha=0.3,
    )

    plt.tight_layout()

    save_figure(
        f"{dataset}_runtime"
    )


# ============================================================
# GRÁFICA: MEMORIA
# ============================================================

def plot_memory(
    benchmark,
    dataset,
):
    """
    Gráfica de memoria pico.
    """

    summary = (
        benchmark
        .groupby("operator")
        .agg(
            mean=(
                "memory_peak_mb",
                "mean",
            ),

            std=(
                "memory_peak_mb",
                "std",
            ),
        )
        .reset_index()
    )

    summary = order_operators(
        summary
    )

    plt.figure(
        figsize=(10, 6)
    )

    x = np.arange(
        len(summary)
    )

    plt.bar(
        x,
        summary["mean"],
        yerr=summary["std"],
        capsize=4,
    )

    plt.xticks(
        x,
        summary["operator"],
        rotation=35,
        ha="right",
    )

    plt.ylabel(
        "Memoria pico (MB)"
    )

    plt.xlabel(
        "Operador"
    )

    plt.title(
        f"Uso de memoria — {DATASETS[dataset]}"
    )

    plt.grid(
        axis="y",
        alpha=0.3,
    )

    plt.tight_layout()

    save_figure(
        f"{dataset}_memory"
    )


# ============================================================
# GRÁFICA: F1
# ============================================================

def plot_f1(
    metrics,
    dataset,
):
    """
    Gráfica del F1 promedio.

    Si un operador tiene varios parámetros,
    cada configuración aparece por separado.
    """

    summary = (
        metrics
        .groupby(
            [
                "operator",
                "parameter",
            ]
        )
        .agg(
            mean=(
                "structure_f1",
                "mean",
            ),

            std=(
                "structure_f1",
                "std",
            ),
        )
        .reset_index()
    )

    summary = order_operators(
        summary
    )

    labels = [
        f"{operator}\n({parameter})"
        for operator, parameter in zip(
            summary["operator"],
            summary["parameter"],
        )
    ]

    plt.figure(
        figsize=(12, 6)
    )

    x = np.arange(
        len(summary)
    )

    plt.bar(
        x,
        summary["mean"],
        yerr=summary["std"],
        capsize=3,
    )

    plt.xticks(
        x,
        labels,
        rotation=45,
        ha="right",
    )

    plt.ylabel(
        "F1"
    )

    plt.xlabel(
        "Operador y configuración"
    )

    plt.title(
        f"F1 promedio — {DATASETS[dataset]}"
    )

    plt.grid(
        axis="y",
        alpha=0.3,
    )

    plt.tight_layout()

    save_figure(
        f"{dataset}_f1"
    )


# ============================================================
# GRÁFICA: F1 VS LOCALIZACIÓN
# ============================================================

def plot_f1_vs_localization(
    metrics,
    dataset,
):
    """
    Relación entre F1 y error de localización.

    F1 alto y error bajo representan mejor desempeño.
    """

    summary = (
        metrics
        .groupby(
            [
                "operator",
                "parameter",
            ]
        )
        .agg(
            f1=(
                "structure_f1",
                "mean",
            ),

            localization=(
                "localization_error",
                "mean",
            ),
        )
        .reset_index()
    )

    plt.figure(
        figsize=(9, 7)
    )

    plt.scatter(
        summary["localization"],
        summary["f1"],
        s=70,
    )

    for _, row in summary.iterrows():

        label = (
            f"{row['operator']}"
            f" ({row['parameter']})"
        )

        plt.annotate(
            label,
            (
                row["localization"],
                row["f1"],
            ),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
        )

    plt.xlabel(
        "Error de localización"
    )

    plt.ylabel(
        "F1"
    )

    plt.title(
        f"F1 vs. error de localización — "
        f"{DATASETS[dataset]}"
    )

    plt.grid(
        alpha=0.3,
    )

    plt.tight_layout()

    save_figure(
        f"{dataset}_f1_vs_localization"
    )


# ============================================================
# HEATMAP F1
# ============================================================



def plot_f1_heatmap(
    metrics,
    dataset,
):
    """
    Genera un heatmap de F1 por imagen y operador.

    Para operadores parametrizados se selecciona,
    para cada operador, la configuración con mayor
    F1 promedio sobre todas las imágenes.
    """

    # ========================================================
    # Mejor parámetro por operador
    # ========================================================

    parameter_summary = (
        metrics
        .groupby(
            ["operator", "parameter"]
        )
        .agg(
            f1=("structure_f1", "mean")
        )
        .reset_index()
    )

    best_parameters = (
        parameter_summary
        .loc[
            parameter_summary
            .groupby("operator")["f1"]
            .idxmax()
        ]
        .set_index("operator")["parameter"]
        .to_dict()
    )

    # ========================================================
    # Seleccionar mejor configuración
    # ========================================================

    selected = []

    for operator, parameter in best_parameters.items():

        subset = metrics[
            (metrics["operator"] == operator)
            &
            (metrics["parameter"] == parameter)
        ].copy()

        selected.append(subset)

    if not selected:
        raise ValueError(
            "No hay datos para generar el heatmap."
        )

    selected = pd.concat(
        selected,
        ignore_index=True,
    )

    # ========================================================
    # Matriz operador × imagen
    # ========================================================

    pivot = selected.pivot_table(
        index="operator",
        columns="image",
        values="structure_f1",
        aggfunc="mean",
    )

    # Ordenar operadores
    pivot = pivot.reindex(
        [
            operator
            for operator in OPERATOR_ORDER
            if operator in pivot.index
        ]
    )

    # Ordenar imágenes
    pivot = pivot.reindex(
        sorted(pivot.columns),
        axis=1,
    )

    # ========================================================
    # DEBUG
    # ========================================================

    print("\nMATRIZ DEL HEATMAP:")
    print(pivot.to_string())

    # ========================================================
    # Crear figura
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(11, 6)
    )

    # ========================================================
    # Heatmap
    # ========================================================

    heatmap = ax.imshow(
        pivot.values,
        aspect="auto",
        vmin=0,
        vmax=1,
        interpolation="nearest",
    )

    # ========================================================
    # Barra de color
    # ========================================================

    fig.colorbar(
        heatmap,
        ax=ax,
        label="F1",
    )

    # ========================================================
    # Ejes
    # ========================================================

    ax.set_xticks(
        np.arange(
            len(pivot.columns)
        )
    )

    ax.set_xticklabels(
        pivot.columns,
        rotation=45,
        ha="right",
    )

    ax.set_yticks(
        np.arange(
            len(pivot.index)
        )
    )

    ax.set_yticklabels(
        pivot.index
    )

    ax.set_xlabel(
        "Imagen"
    )

    ax.set_ylabel(
        "Operador"
    )

    ax.set_title(
        f"F1 por imagen y operador — "
        f"{DATASETS[dataset]}"
    )

    # ========================================================
    # VALORES
    # ========================================================

    for row in range(pivot.shape[0]):

        for col in range(pivot.shape[1]):

            value = pivot.iloc[row, col]

            if pd.isna(value):
                text = "-"
            else:
                text = f"{value:.3f}"

            ax.annotate(
                text,
                xy=(col, row),
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold",
                zorder=10,
            )

    # ========================================================
    # Líneas de separación
    # ========================================================

    ax.set_xticks(
        np.arange(
            -0.5,
            len(pivot.columns),
            1,
        ),
        minor=True,
    )

    ax.set_yticks(
        np.arange(
            -0.5,
            len(pivot.index),
            1,
        ),
        minor=True,
    )

    ax.grid(
        which="minor",
        linestyle="-",
        linewidth=0.5,
    )

    ax.tick_params(
        which="minor",
        bottom=False,
        left=False,
    )

    # ========================================================
    # Guardar
    # ========================================================

    fig.tight_layout()

    save_figure(
        f"{dataset}_f1_heatmap"
    )

# ============================================================
# GENERACIÓN COMPLETA
# ============================================================

def generate_dataset_report(
    dataset,
):
    """
    Genera todas las tablas y gráficas
    correspondientes a un dataset.
    """

    print(
        f"\nGenerando reporte: "
        f"{DATASETS[dataset]}"
    )

    # ========================================================
    # Cargar resultados
    # ========================================================

    metrics, benchmark = (
        load_results(dataset)
    )

    # ========================================================
    # Tablas
    # ========================================================

    create_benchmark_table(
        benchmark,
        dataset,
    )

    create_metrics_table(
        metrics,
        dataset,
    )

    create_best_f1_table(
        metrics,
        dataset,
    )

    # ========================================================
    # Gráficas
    # ========================================================

    plot_runtime(
        benchmark,
        dataset,
    )

    plot_memory(
        benchmark,
        dataset,
    )

    plot_f1(
        metrics,
        dataset,
    )

    plot_f1_vs_localization(
        metrics,
        dataset,
    )

    plot_f1_heatmap(
        metrics,
        dataset,
    )

    print(
        f"Reporte generado correctamente: "
        f"{DATASETS[dataset]}"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    prepare_directories()

    for dataset in DATASETS:

        generate_dataset_report(
            dataset
        )

    print(
        "\n========================================"
    )

    print(
        "Reporte completo generado."
    )

    print(
        f"Tablas:  {TABLES_DIR}"
    )

    print(
        f"Figuras: {FIGURES_DIR}"
    )

    print(
        "========================================"
    )


if __name__ == "__main__":
    main()
