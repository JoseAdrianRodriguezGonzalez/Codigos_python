import numpy as np 
from operadores.kernels import PREWITT_X,PREWITT_Y
from operadores.gradient import apply_gradient_kernels
def prewitt(image):
    return apply_gradient_kernels(image,PREWITT_X,PREWITT_Y)
