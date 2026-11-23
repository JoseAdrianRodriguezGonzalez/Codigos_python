
from preparacion.comprobacion import report
from preparacion.generate_dataset import main_p
from preparacion.normalizacion import (
    load_images,
    conversion2gray,
    normalize1,
)
from preparacion.plots import (
    plot_image_with_histogram,
)
from preparacion.ruido import (
    noise_generation,
)
from preparacion.ground_truth import (
    load_bsds_ground_truth,
)

def preparacion_pipeline(args):

    # ==========================================
    # Generación
    # ==========================================

    if args.generate:
        main_p()

    # ==========================================
    # Reportes
    # ==========================================

    df_synthetic = report(
        "synthetic_dataset",
        "output/image_report_synthetic.csv",
        "output/image_report_synthetic.tex",
    )

    df_complex = report(
        "data",
        "output/image_report_bsds.csv",
        "output/image_report_bsds.tex",
    )
    bsds_ground_truth = load_bsds_ground_truth(
        df_complex,
        "data/ground_truth",
    )
    # ==========================================
    # Synthetic
    # ==========================================

    df_synthetic_images = (
        df_synthetic[
            df_synthetic["filename"] == "clean.jpg"
        ]
        .copy()
        .sort_values("directory")
        .reset_index(drop=True)
    )

    df_synthetic_gt = (
        df_synthetic[
            df_synthetic["filename"]
            == "ground_truth.jpg"
        ]
        .copy()
        .sort_values("directory")
        .reset_index(drop=True)
    )

    # ==========================================
    # Cargar imágenes synthetic
    # ==========================================

    list_synthetic = load_images(
        df_synthetic_images,
        "relative_path",
        df_synthetic_images["root"].iloc[0],
    )

    list_synthetic_gt = load_images(
        df_synthetic_gt,
        "relative_path",
        df_synthetic_gt["root"].iloc[0],
    )

    # ==========================================
    # BSDS
    # ==========================================

    df_complex = (
        df_complex
        .sort_values("filename")
        .reset_index(drop=True)
    )

    list_complex = load_images(
        df_complex,
        "relative_path",
        df_complex["root"].iloc[0],
    )

    # ==========================================
    # Escala de grises
    # ==========================================

    list_synthetic = [
        conversion2gray(img)
        for img in list_synthetic
    ]

    list_synthetic_gt = [
        conversion2gray(img)
        for img in list_synthetic_gt
    ]

    list_complex = [
        conversion2gray(img)
        for img in list_complex
    ]

    # ==========================================
    # Normalización
    # ==========================================

    synthetic_normalized = normalize1(
        list_synthetic
    )

    complex_normalized = normalize1(
        list_complex
    )

    # ==========================================
    # Nombres
    # ==========================================

    synthetic_names = (
        df_synthetic_images[
            "directory"
        ].tolist()
    )

    bsds_names = (
        df_complex["filename"]
        .str.replace(
            ".jpg",
            "",
            regex=False,
        )
        .tolist()
    )

    # ==========================================
    # Ground truth como diccionario
    # ==========================================

    if len(synthetic_names) != len(
        list_synthetic_gt
    ):
        raise ValueError(
            "El número de imágenes sintéticas "
            "no coincide con el número de ground truths."
        )

    synthetic_ground_truth = {
        name: ground_truth
        for name, ground_truth in zip(
            synthetic_names,
            list_synthetic_gt,
        )
    }

    # ==========================================
    # Visualización
    # ==========================================

    if args.plots:

        image_list = (
            list_complex
            + list_synthetic
        )

        for image in image_list:
            plot_image_with_histogram(
                image
            )

    # ==========================================
    # Ruido
    # ==========================================

    if args.generate:

        noise_generation(
            synthetic_names,
            list_synthetic,
            "output/noisy/synthetic",
        )

        noise_generation(
            bsds_names,
            list_complex,
            "output/noisy/bsds",
        )

    # ==========================================
    # Resultado
    # ==========================================
    return {

        "synthetic": {
            "names": synthetic_names,
            "images": list_synthetic,
            "normalized": synthetic_normalized,
            "ground_truth": synthetic_ground_truth,
        },

        "bsds": {
            "names": bsds_names,
            "images": list_complex,
            "normalized": complex_normalized,
            "ground_truth": bsds_ground_truth,
        },

        "metadata": {
            "synthetic": df_synthetic,
            "bsds": df_complex,
        },
    }
