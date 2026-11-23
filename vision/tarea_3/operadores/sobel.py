import numpy as np 
from operadores.kernels import SOBEL_X,SOBEL_Y
from operadores.gradient import apply_gradient_kernels
def sobel(image):
    return apply_gradient_kernels(image,SOBEL_X,SOBEL_Y)
