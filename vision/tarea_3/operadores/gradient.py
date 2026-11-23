import cv2
import numpy as np 
def apply_gradient_kernels(image,kernel_x,kernel_y):
    gx=cv2.filter2D(image,cv2.CV_32F,kernel_x)
    gy=cv2.filter2D(image,cv2.CV_32F,kernel_y)
    return gx,gy 
def gradient_magnitude(gx,gy):
    return np.sqrt(gx**2+gy**2)
def threshold_gradient(magnitude,threshold):
    return (magnitude>threshold).astype(np.uint8)*255
