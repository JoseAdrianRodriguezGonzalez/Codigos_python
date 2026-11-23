import os
import cv2
import numpy as  np
import pickle
import matplotlib.pyplot as plt 

ROOT="DIP3E_Original_Images_CH01"
def save_image(image, path):
    cv2.imwrite(path, image)
def save_histogram(hist, path, title):
    plt.figure()
    plt.plot(hist)
    plt.title(title)
    plt.xlabel("Intensidad")
    plt.ylabel("Frecuencia")
    plt.xlim([0, 256])
    plt.savefig(path, bbox_inches="tight")
    plt.close()
def histogram(img):
    return cv2.calcHist([img],[0],None,[256],[0,256])
def first_task():
    images=[os.path.join(ROOT,images) for images in os.listdir(ROOT) if not images.endswith(".txt")]
    full={"original":[],
          "histogram":[],
          "equalized":[],
          "histogram_eq":[]}
    for image in images:
        img = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        hist_gray=histogram(img) 
        equalized = cv2.equalizeHist(img)
        full["original"].append(img)
        full["histogram"].append(hist_gray)
        full["equalized"].append(equalized)
        full["histogram_eq"].append(histogram(equalized))
    return full
#transformaciones
#Lineal 
def lineal(img,alpha,beta):
    return np.clip(alpha*img+beta,0,255).astype(np.uint8)
def logarithm(img):
    img_float=img.astype(np.float32)
    c= 255/np.log(1+img_float.max())
    transformed=c*np.log(1+img_float)
    return transformed.astype(np.uint8)
def gamma(img,gamma):
    img_float=img.astype(np.uint32)/255.0 
    transformed=255 * (img_float**gamma)
    return transformed.astype(np.uint8)
    
def second_task():
    images=[os.path.join(ROOT,images) for images in os.listdir(ROOT) if not images.endswith(".txt")]
    histograms={"normal":[],
                "lineal":[],
                "log":[],
                "gamma":[]}
    original={"normal":[],
                "lineal":[],
                "log":[],
                "gamma":[]}
    for image in images:
        img = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        img_lineal = lineal(img, 1, 1)
        img_log = logarithm(img)
        img_gamma = gamma(img, 1.0)

        original["normal"].append(img)
        original["lineal"].append(img_lineal)
        original["log"].append(img_log)
        original["gamma"].append(img_gamma)
        histograms["normal"].append(histogram(img))
        histograms["lineal"].append(histogram(img_lineal))
        histograms["log"].append(histogram(img_log))
        histograms["gamma"].append(histogram(img_gamma))
    return histograms,original
def read_data():
    with open("cifar-10-batches-py/data_batch_1","rb") as f:
        batch = pickle.load(f,encoding="bytes")
    data=batch[b"data"]
    return data 
def take_image(data,index):
    image=data[index].reshape(3,32,32)
    return np.transpose(image,(1,2,0))
def format(format,image):
    if format =="HSV":
        return cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    elif format=="YCbCr":
        return cv2.cvtColor(image,cv2.COLOR_RGB2YCrCb)
    elif format=="LAB":
        return cv2.cvtColor(image,cv2.COLOR_RGB2LAB)
    elif format=="RGB":
        return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
def show_channel(image, channel, title,filename):
    channel_image = image[:, :, channel]

    cv2.imshow(title, channel_image)
    cv2.imwrite(filename, channel_image)
    
def third_task():
    data=read_data() 
    print(data.shape) 
    img=take_image(data,np.random.choice(data.shape[0],1,replace=False))   
    img_rgb=format("RGB",img)
    img_hsv=format("HSV",img_rgb)
    img_ycbcr = format("YCbCr",img_rgb)
    img_lab=format("LAB",img_rgb)
    
    show_channel(img_hsv, 0, "HSV - H","output/task3/HSV_H.png")
    show_channel(img_hsv, 1, "HSV - S","output/task3/HSV_S.png")
    show_channel(img_hsv, 2, "HSV - V","output/task3/HSV_V.png")

    show_channel(img_ycbcr, 0, "YCrCb - Y","output/task3/YCRCB_Y.png")
    show_channel(img_ycbcr, 1, "YCrCb - Cr","output/task3/YCRCB_CR.png")
    show_channel(img_ycbcr, 2, "YCrCb - Cb","output/task3/YCRCB_CB.png")

    show_channel(img_lab, 0, "LAB - L","output/task3/LAB_L.png")
    show_channel(img_lab, 1, "LAB - a","output/task3/LAB_A.png")
    show_channel(img_lab, 2, "LAB - b","output/task3/LAB_B.png")

def save_first_task(full):
    index = np.random.choice(len(full["original"]))
    os.makedirs("output/task1", exist_ok=True)
    save_image(
        full["original"][index],
        "output/task1/original.png"
    )

    save_histogram(
        full["histogram"][index],
        "output/task1/histogram.png",
        "Histograma original"
    )

    save_image(
        full["equalized"][index],
        "output/task1/equalized.png"
    )

    save_histogram(
        full["histogram_eq"][index],
        "output/task1/histogram_equalized.png",
        "Histograma ecualizado"
    )

    print(f"Índice seleccionado: {index}")
def save_second_task(histograms, images):
    index = np.random.choice(len(images["normal"]))

    os.makedirs("output/task2", exist_ok=True)

    transformations = ["normal", "lineal", "log", "gamma"]

    for transformation in transformations:

        save_image(
            images[transformation][index],
            f"output/task2/{transformation}.png"
        )

        save_histogram(
            histograms[transformation][index],
            f"output/task2/histogram_{transformation}.png",
            f"Histograma - {transformation}"
        )

    print(f"Índice seleccionado: {index}")

def main():
    os.makedirs("output",exist_ok=True)
    os.makedirs("output/task3",exist_ok=True)
    full=first_task()
    save_first_task(full)
    histograms2,images=second_task()
    save_second_task(histograms2,images)
    third_task()
main()
