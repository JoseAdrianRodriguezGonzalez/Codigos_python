import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
import os 
def read_images(src):

    image=cv2.imread(src)
    if image is None:
        raise ValueError("No se puede leer la imagen")
    return image
def convert2grey(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
def save_plots(output,data,cmap):
    plt.imshow(data, cmap=cmap)
    plt.title("Imagen en escala de grises")
    plt.axis("off")
    plt.savefig(output)
def histogram(data, output):
    if data.ndim == 2:
        channels = [0]
        labels = ["Gray"]
    else:
        channels = [0, 1, 2]
        labels = ["Blue", "Green", "Red"]
    histograms = []
    plt.figure()
    for channel, label in zip(channels, labels):
        hist = cv2.calcHist([data],[channel],None,[256],[0, 256])
        histograms.append(hist)
        plt.plot(hist, label=label)
    plt.title("Histograma de la imagen")
    plt.xlabel("Intensidad")
    plt.ylabel("Número de píxeles")
    plt.xlim([0, 256])
    if len(channels) > 1:
        plt.legend()
    plt.savefig(output)
    plt.close()
    return histograms[0] if data.ndim == 2 else histograms
def preprocessing(cloudy,sunset,mode):
    if mode=="gray":
        #convertir a gris 
        cloudy_grey=convert2grey(cloudy)
        sunset_grey=convert2grey(sunset)
        os.makedirs("results/gray",exist_ok=True)
        save_plots("results/gray/cloudy_gray.png",cloudy_grey,"gray")
        save_plots("results/gray/sunset_gray.png",sunset_grey,"gray")
        #histograma de color 
        cloudy_hist=histogram(cloudy_grey,"results/gray/cloudy_histogram.png")
        sunset_hist=histogram(sunset_grey,"results/gray/sunset_histogram.png")
        
    elif mode=="color":
        os.makedirs("results/bgr",exist_ok=True)
        #histograma de color 
        cloudy_hist=histogram(cloudy,"results/bgr/cloudy_hist.png")    
        sunset_hist=histogram(sunset,"results/bgr/sunset_hist.png")    
    else:
        raise ValueError("No existe eso")
    return cloudy_hist,sunset_hist
  
def cumulative_transform(hist):
    pdf=hist.ravel().astype(np.float64)
    pdf /=pdf.sum()
    cdf=np.cumsum(pdf)
    return cdf 
def histogram_specification(source_hist,reference_hist):
    source_cdf=cumulative_transform(source_hist)
    reference_cdf=cumulative_transform(reference_hist)
    lookup_table=np.zeros(256,dtype=np.uint8)
    for r in range(256):
        lookup_table[r]=np.argmin(np.abs(reference_cdf-source_cdf[r]))
    return lookup_table
def apply_specification(image,lookup_table):
    return cv2.LUT(image,lookup_table)
def transformation(image,histogram_source,histogram_reference,mode):
    if mode=="gray":
        lookup_table=histogram_specification(histogram_source,histogram_reference)
        specified=apply_specification(image,lookup_table)
        cv2.imwrite("results/gray/spec.png",specified)
        histogram(convert2grey(specified),"results/gray/image_specified_histogram.png")
    elif mode=="color":
        specified=image.copy()
        for channel in range(3):
            lookup_table=histogram_specification(histogram_source[channel],histogram_reference[channel])
            specified[:,:,channel]=apply_specification(image[:,:,channel],lookup_table)
        cv2.imwrite("results/bgr/spec.png", specified)
        histogram(specified, "results/bgr/image_specified_histogram.png")
    else:
        raise ValueError("Modo no válido. Usa 'gray' o 'color'.")
    return specified
def main():
    #lectura de imagenes 
    os.makedirs("results",exist_ok=True)
    os.makedirs("data",exist_ok=True)
    images=["data/cloudy.png","data/sunset.png"]
    cloudy=read_images(images[0])
    sunset=read_images(images[1])
    #preprocesamiento 
    cloudy_g,sunset_g=preprocessing(cloudy,sunset,"gray")
    cloudy_bgr,sunset_bgr=preprocessing(cloudy,sunset,"color")
    #transformacion 
    transformation(cloudy,cloudy_g,sunset_g,"gray")
    transformation(cloudy,cloudy_bgr,sunset_bgr,"color")
     
   
main()
