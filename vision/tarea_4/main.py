import pandas as pd 
import os
import re
from collections import defaultdict

DATASET_DIR = "coil-100"
NUM_OBJECTS = 20

##Leer los conjuntos de datos 
def dataset_images():
# Formato esperado: obj1__0.png
    pattern = re.compile(r"^obj(\d+)__(\d+)\.(?:png|jpg|jpeg)$", re.IGNORECASE)
    rows=[]
    for filename in os.listdir(DATASET_DIR):
        match = pattern.match(filename)

        if not match:
            continue

        object_id = int(match.group(1))
        view_id = int(match.group(2))

        if 1 <= object_id <= NUM_OBJECTS:
            path_image=os.path.join(DATASET_DIR, filename)
            
            rows.append({
                "path":path_image,
                "label":f"obj{object_id}",
                "object_id":object_id,
                "view_id":view_id
            })
    df =pd.DataFrame(rows)
    df =df.sort_values(["object_id","view_id"]).reset_index(drop=True)
    counts=df.groupby("object_id").size()
    for object_id in range(1, NUM_OBJECTS + 1):
        count = counts.get(object_id, 0)
        print(f"Objeto {object_id:02d}: {count:2d} imágenes")

    print(f"\nObjetos encontrados: {df['object_id'].nunique()}")
    print(f"Imágenes encontradas: {len(df)}")
    print(f"Imágenes esperadas: {NUM_OBJECTS * 72}")
    return df
# realizar el split sugerido 
import numpy as np 
def split(df,n_reference=16):
    references=[]
    tests=[]
    for object_id,group in df.groupby("object_id"):
        group=group.sort_values("view_id").reset_index(drop=True)
        if len(group)!=72:
            raise ValueError(f"Objecto {object_id}: se esperan 72 imagenes, pero hay {len(group)}")
        indices=np.linspace(0,len(group)-1,n_reference,dtype=int)
        reference=group.iloc[indices]
        test=group.drop(index=indices)
        references.append(reference)
        tests.append(test)
    references_df=pd.concat(references,ignore_index=True)
    test_df=pd.concat(tests,ignore_index=True)
    return references_df,test_df
#se extraen histogramas acorde al espacio de color 
import cv2 
def extract_color_features(image_path,color_space,bins=8):
    image=cv2.imread(image_path)
    if image is None:
        raise ValueError(f"NO se puedo cargar: {image_path}")
    if color_space == "RGB":
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        ranges=[0,256,0,256,0,256]
    elif color_space == "HSV":
        image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)    
        ranges=[0,180,0,256,0,256]
        
    elif color_space == "CIELAB":
        image=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
        ranges=[0,256,0,256,0,256]
    else:
        raise ValueError(f"Espacio no soportado : {color_space}")
    hist=cv2.calcHist([image],[0,1,2],None,[bins,bins,bins],ranges)
    hist=cv2.normalize(hist,hist,norm_type=cv2.NORM_L1)
    return hist.flatten() 
def build_feature_dataset(df,color_space,bin=8):
    features=np.stack([
        extract_color_features(path,color_space,bins=bin) for path in df["path"]
    ])
    feature_df=pd.DataFrame({
        "path": df["path"].to_numpy(),
        "label": df["label"].to_numpy(),
        "object_id": df["object_id"].to_numpy(),
        "view_id": df["view_id"].to_numpy(),
    })
    return features,feature_df 
#Se hace el pequeño modelo 
from sklearn.metrics import pairwise_distances 
def predict_nearest(reference_features,reference_df,test_features,metric="euclidean"):
    distances=pairwise_distances(test_features,reference_features,metric=metric)
    nearest_indices=np.argmin(distances,axis=1)
    predictions=reference_df["label"].to_numpy()[nearest_indices]
    confidence_distances=distances[np.arange(len(test_features)),nearest_indices]
    return predictions,confidence_distances
#metricas 
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,f1_score,recall_score
def evaluate_predictions(y_true,y_pred,class_labels):
    cm = confusion_matrix(y_true,y_pred,labels=class_labels)
    total = cm.sum()
    class_results = []
    for i, label in enumerate(class_labels):
        tp = int(cm[i, i])
        fp = int(cm[:, i].sum() - tp)
        fn = int(cm[i, :].sum() - tp)
        tn = int(total - tp - fp - fn)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = (2 * precision * recall / (precision + recall)
            if precision + recall else 0.0
        )
        class_results.append({
            "class": label,
            "TP": tp,
            "FP": fp,
            "FN": fn,
            "TN": tn,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        })

    accuracy = accuracy_score(y_true, y_pred)

    global_results = {
        "accuracy": accuracy,
        "recognition_rate": accuracy,
        "error": 1 - accuracy,
        "precision_macro": precision_score(
            y_true, y_pred,
            labels=class_labels,
            average="macro",
            zero_division=0
        ),
        "recall_macro": recall_score(
            y_true, y_pred,
            labels=class_labels,
            average="macro",
            zero_division=0
        ),
        "f1_macro": f1_score(
            y_true, y_pred,
            labels=class_labels,
            average="macro",
            zero_division=0
        )
    }

    return global_results, pd.DataFrame(class_results), cm
import os
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(y_true,y_pred,class_labels,color_space,output_dir="results/confusion_matrices"):
    os.makedirs(output_dir, exist_ok=True)
    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=class_labels
    )

    fig, ax = plt.subplots(figsize=(14, 12))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=class_labels,
        yticklabels=class_labels,
        linewidths=0.3,
        ax=ax
    )

    ax.set_title(f"Matriz de confusión - {color_space}")
    ax.set_xlabel("Clase predicha")
    ax.set_ylabel("Clase real")

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    plt.setp(ax.get_yticklabels(), rotation=0)

    fig.tight_layout()

    output_path = os.path.join(
        output_dir,
        f"confusion_matrix_{color_space.lower()}.png"
    )

    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Matriz guardada: {output_path}")

    return cm
def main():
    dataset=dataset_images()
    reference_df,test_df=split(dataset)
    spaces = ["RGB", "HSV", "CIELAB"]
    class_labels = [f"obj{i}" for i in range(1, NUM_OBJECTS + 1)]
    global_results = []
    class_results = []
    for space in spaces:
        reference_features, _ = build_feature_dataset(reference_df, space)
        test_features, _ = build_feature_dataset(test_df, space)

        predictions, distances = predict_nearest(reference_features,reference_df,test_features)

        y_true = test_df["label"].to_numpy()
        y_pred = predictions
        metrics, per_class, _ = evaluate_predictions(y_true,y_pred,class_labels)
        cm = plot_confusion_matrix(
            y_true=test_df["label"].to_numpy(),
            y_pred=predictions,
            class_labels=class_labels,
            color_space=space
        )
        # Resultados globales por espacio de color
        global_results.append({"color_space": space,**metrics})
        # Resultados individuales por objeto
        per_class.insert(0, "color_space", space)
        class_results.append(per_class)
        print("\nMétricas globales:")
        for name, value in metrics.items():
            print(f"{name}: {value:.4f} ({value * 100:.2f}%)")
        print("\nMétricas por clase:")
        print(per_class.to_string(index=False))
        print("\nMatriz de confusión:")
        print(cm)
    global_df = pd.DataFrame(global_results)
    classes_df = pd.concat(class_results, ignore_index=True)
    print("\nRESUMEN GLOBAL")
    print(global_df.to_string(index=False))
    global_df.to_csv("global_metrics.csv", index=False)
    classes_df.to_csv("class_metrics.csv", index=False)
    print("\nResultados guardados en:")
    print("- global_metrics.csv")
    print("- class_metrics.csv")

main()
