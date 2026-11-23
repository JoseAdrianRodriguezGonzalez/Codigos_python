from operadores.gradient import gradient_magnitude, threshold_gradient


def detect_edges(image,detector,threshold):
    gx,gy=detector(image)
    magnitude=gradient_magnitude(gx,gy)
    edges=threshold_gradient(magnitude,threshold)
    return {
        "gx":gx,
        "gy":gy,
        "magnitude":magnitude,
        "edges":edges
    }
from operadores.roberts import roberts 
from operadores.prewitt import prewitt
from operadores.scharr import scharr 
from operadores.sobel import sobel 
detectors={
    "roberts":roberts,
    "prewitt":prewitt,
    "scharr":scharr,
    "sobel":sobel
}
SECOND_ORDER_SIGMAS = [1.0, 2.0, 3.0]
from operadores.laplacian import laplacian
from operadores.log import log
import numpy as np
from operadores.second_order import zero_crossing
from operadores.canny import canny
CANNY_RATIOS = [
    (50, 75),
    (50, 100),
    (50, 150),
]
def detect_laplacian(image,zero_threshold = 0.0):
    response = laplacian(image)
    edges = zero_crossing(response,threshold=zero_threshold)
    return {
        "response": response,
        "edges": edges,
    }
def detect_log(image,sigma, zero_threshold= 0.0):
    response, edges = log(image,sigma=sigma,zero_threshold=zero_threshold)
    return {
        "response": response,
        "edges": edges,
    }

def detect_canny(
    image,
    sigma=1.0,
):

    results = {}

    for tlow, thigh in CANNY_RATIOS:

        ratio = thigh / tlow

        results[ratio] = canny(
            image,
            sigma=sigma,
            tlow=tlow,
            thigh=thigh,
        )
    return results

from operadores.derichie import deriche


DERICHE_ALPHAS = [
    0.5,
    1.0,
    2.0,
    4.0,
]


def detect_deriche( image: np.ndarray, threshold=50, ) -> dict:
    results = {} 
    for alpha in DERICHE_ALPHAS: 
        result = deriche( image, alpha=alpha, ) 
        magnitude = result["magnitude"]
        edges = ( magnitude >= threshold ).astype(np.uint8) * 255 
        results[alpha] = { 
            "gx": result["gx"], 
            "gy": result["gy"], 
            "magnitude": magnitude, 
            "direction": result["direction"], 
            "edges": edges, } 
    return results

def pipeline_detectors(
    image,
    threshold=50,
):

    results = {}

    # -------------------------
    # Primera derivada
    # -------------------------

    for name, detector in detectors.items():

        results[name] = detect_edges(
            image,
            detector,
            threshold,
        )

    # -------------------------
    # Laplaciano
    # -------------------------

    results["laplacian"] = detect_laplacian(
        image,
        zero_threshold=0.0,
    )

    # -------------------------
    # LoG
    # -------------------------

    results["log"] = {}

    for sigma in SECOND_ORDER_SIGMAS:

        results["log"][sigma] = detect_log(
            image,
            sigma=sigma,
            zero_threshold=0.0,
        )

    # -------------------------
    # Canny
    # -------------------------

    results["canny"] = detect_canny(
        image,
        sigma=1.0,
    )
    results["deriche"] = detect_deriche(
        image
    )

    return results

