import cv2
import numpy as np

from operadores.kernels import LAPLACIAN_KERNEL
from operadores.second_order import zero_crossing

def log(image,sigma,zero_threshold = 0.0,):

    blurred = cv2.GaussianBlur(image,ksize=(0, 0),sigmaX=sigma,sigmaY=sigma,)
    laplacian = cv2.filter2D(blurred,cv2.CV_32F,LAPLACIAN_KERNEL,)
    edges = zero_crossing(laplacian,threshold=zero_threshold,)
    return laplacian, edges
