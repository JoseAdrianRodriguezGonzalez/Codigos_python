import cv2 
import os 
def load_images(df,column,root):
    images=[]

    for idx,row in enumerate(df[column]):

        path=os.path.join(root,row)
        image=cv2.imread(path,cv2.IMREAD_UNCHANGED)
        if image is None:
            raise ValueError(f"Error al leer la imagen {path}")
        images.append(image)
    return images 
def conversion2gray(img):
    if len(img.shape) ==3:
        if img.shape[2]==3:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        elif img.shape[2]==4:
            img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
        else:
            raise ValueError(f" cantidad de canales no soportado ({img.shape[2]})")
    elif len(img.shape)!=2:
        raise ValueError(f" forma de imagen no soportada ({img.shape}) ")
    return img
def normalize1(listimg):
    return [img.astype("float32")/255.0 for img in listimg]

