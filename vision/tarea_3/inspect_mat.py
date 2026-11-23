from scipy.io import loadmat


data = loadmat(
    "data/ground_truth/20008.mat"
)

gt = data["groundTruth"]

print("shape:", gt.shape)
print("dtype:", gt.dtype)

print(
    "\nNúmero de elementos:",
    gt.size,
)

for i in range(gt.size):

    annotation = gt.flat[i]

    print(
        f"\n===== Anotación {i + 1} ====="
    )

    print(
        "type:",
        type(annotation),
    )

    print(
        "shape:",
        annotation.shape,
    )

    print(
        "dtype:",
        annotation.dtype,
    )

    print(
        "dtype names:",
        annotation.dtype.names,
    )

    print(
        "Segmentation shape:",
        annotation["Segmentation"][0, 0].shape,
    )

    print(
        "Segmentation dtype:",
        annotation["Segmentation"][0, 0].dtype,
    )

    print(
        "Boundaries shape:",
        annotation["Boundaries"][0, 0].shape,
    )

    print(
        "Boundaries dtype:",
        annotation["Boundaries"][0, 0].dtype,
    )

    print(
        "Edge pixels:",
        annotation["Boundaries"][0, 0].sum(),
    )


