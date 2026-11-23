import os

import cv2
import numpy as np
from scipy.io import loadmat


def load_bsds_ground_truth(
    dataframe,
    root,
    consensus=0.5,
):
    """
    Carga y agrega las anotaciones de ground truth
    del dataset BSDS500.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        DataFrame con las imágenes BSDS.

    root : str
        Directorio raíz que contiene los archivos .mat.

    consensus : float
        Proporción mínima de anotadores que deben
        marcar un píxel como borde.

        Por defecto:
            0.5 = mayoría de los anotadores.

    Returns
    -------
    dict
        Diccionario:

        {
            "20008": ground_truth,
            "24004": ground_truth,
            ...
        }
    """

    ground_truth = {}

    for _, row in dataframe.iterrows():

        image_name = row["filename"]

        image_id = os.path.splitext(
            image_name
        )[0]

        mat_path = os.path.join(
            root,
            f"{image_id}.mat",
        )

        if not os.path.exists(mat_path):
            raise FileNotFoundError(
                f"No existe ground truth: {mat_path}"
            )

        data = loadmat(mat_path)

        annotations = data["groundTruth"]

        boundary_maps = []

        for annotation in annotations.flat:

            boundaries = annotation[
                "Boundaries"
            ][0, 0]

            boundaries = (
                boundaries > 0
            )

            boundary_maps.append(
                boundaries
            )

        if not boundary_maps:
            raise ValueError(
                f"No se encontraron anotaciones "
                f"en {mat_path}"
            )

        boundary_maps = np.asarray(
            boundary_maps,
            dtype=np.uint8,
        )

        number_of_annotators = (
            boundary_maps.shape[0]
        )

        votes = boundary_maps.sum(
            axis=0
        )

        required_votes = int(
            np.ceil(
                number_of_annotators
                * consensus
            )
        )

        aggregated = (
            votes >= required_votes
        )

        ground_truth[image_id] = (
            aggregated.astype(np.uint8)
            * 255
        )

    return ground_truth

