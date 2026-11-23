from functools import partial

from operadores.roberts import roberts
from operadores.prewitt import prewitt
from operadores.sobel import sobel
from operadores.scharr import scharr
from operadores.laplacian import laplacian
from operadores.log import log
from operadores.canny import canny
from operadores.derichie import deriche


BENCHMARK_DETECTORS = {
    "Roberts": roberts,
    "Prewitt": prewitt,
    "Sobel": sobel,
    "Scharr": scharr,

    "Laplacian": laplacian,

    "LoG": partial(
        log,
        sigma=1.0,
    ),

    "Canny": partial(
        canny,
        sigma=1.0,
        tlow=50,
        thigh=100,
    ),

    "Deriche": partial(
        deriche,
        alpha=1.0,
    ),
}
