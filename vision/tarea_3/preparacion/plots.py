import cv2
import numpy as np
import matplotlib.pyplot as plt


def image_histogram(image):
    histogram = cv2.calcHist(
        [image],
        [0],
        None,
        [256],
        [0, 256],
    )

    return histogram
def image_statistics(image):
    return {
        "min": np.min(image),
        "max": np.max(image),
        "mean": np.mean(image),
        "std": np.std(image),
    }


def plot_image(image,title = "Image"):
    plt.figure(figsize=(8, 5))
    plt.imshow(image,cmap="gray",vmin=0,vmax=255)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def plot_histogram(image,title= "Histogram"):
    histogram = image_histogram(image)
    plt.figure(figsize=(8, 5))
    plt.plot(histogram)
    plt.title(title)
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    plt.tight_layout()
    plt.show()


def plot_image_with_histogram(image,title= "Image") :
    histogram = image_histogram(image)
    fig, axes = plt.subplots(1,2,figsize=(12, 5),)
    axes[0].imshow(image,cmap="gray",vmin=0,vmax=255)
    axes[0].set_title(title)
    axes[0].axis("off")
    # Histograma
    axes[1].plot(histogram)
    axes[1].set_title("Intensity histogram")
    axes[1].set_xlabel("Intensity")
    axes[1].set_ylabel("Frequency")
    axes[1].set_xlim([0, 256])
    plt.tight_layout()
    plt.show()
