import numpy as np 
from operadores.kernels import SCHARR_X,SCHARR_Y
from operadores.gradient import apply_gradient_kernels
def scharr(image):
    return apply_gradient_kernels(image,SCHARR_X,SCHARR_Y)
