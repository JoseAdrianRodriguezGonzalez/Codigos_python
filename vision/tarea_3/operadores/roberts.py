import numpy as np 
from operadores.kernels import ROBERTS_X,ROBERTS_Y 
from operadores.gradient import apply_gradient_kernels
def roberts(image):
    return apply_gradient_kernels(image,ROBERTS_X,ROBERTS_Y)
