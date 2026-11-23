import cv2
import numpy as np
from operadores.kernels import LAPLACIAN_KERNEL

def laplacian(image):
    return cv2.filter2D(image,cv2.CV_32F,LAPLACIAN_KERNEL)
