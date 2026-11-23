import numpy as np


# ============================================================
# Coeficientes
# ============================================================

def deriche_coefficients(alpha) :

    if alpha <= 0:
        raise ValueError(
            "alpha must be greater than zero."
        )

    exp_alpha = np.exp(-alpha)
    exp_2alpha = np.exp(-2 * alpha)

    k = (
        (1 - exp_alpha) ** 2
        / (
            1
            + 2 * alpha * exp_alpha
            - exp_2alpha
        )
    )

    # -------------------------
    # Suavizado
    # -------------------------

    smoothing = {
        "a1": k,
        "a2": (
            k
            * exp_alpha
            * (alpha - 1)
        ),
        "a3": (
            k
            * exp_alpha
            * (alpha + 1)
        ),
        "a4": (
            -k
            * exp_2alpha
        ),
        "b1": 2 * exp_alpha,
        "b2": -exp_2alpha,
    }

    # -------------------------
    # Derivada
    # -------------------------

    derivative = {
        "a1": 0.0,
        "a2": 1.0,
        "a3": -1.0,
        "a4": 0.0,
        "b1": 2 * exp_alpha,
        "b2": -exp_2alpha,
    }

    return {
        "k": k,
        "smoothing": smoothing,
        "derivative": derivative,
        "derivative_scale": (
            -(1 - exp_alpha) ** 2
        ),
    }


# ============================================================
# Filtro recursivo 1D
# ============================================================

def recursive_filter_1d(signal,coefficients) :

    a1 = coefficients["a1"]
    a2 = coefficients["a2"]
    a3 = coefficients["a3"]
    a4 = coefficients["a4"]
    b1 = coefficients["b1"]
    b2 = coefficients["b2"]

    signal = np.asarray(
        signal,
        dtype=np.float32,
    )

    n = len(signal)

    causal = np.zeros(
        n,
        dtype=np.float32,
    )

    anticausal = np.zeros(
        n,
        dtype=np.float32,
    )

    # ========================================================
    # Causal: izquierda -> derecha
    # ========================================================

    for i in range(n):

        x0 = signal[i]

        x1 = (
            signal[i - 1]
            if i >= 1
            else 0.0
        )

        y1 = (
            causal[i - 1]
            if i >= 1
            else 0.0
        )

        y2 = (
            causal[i - 2]
            if i >= 2
            else 0.0
        )

        causal[i] = (
            a1 * x0
            + a2 * x1
            + b1 * y1
            + b2 * y2
        )

    # ========================================================
    # Anticausal: derecha -> izquierda
    # ========================================================

    for i in range(n - 1, -1, -1):

        x1 = (
            signal[i + 1]
            if i < n - 1
            else 0.0
        )

        x2 = (
            signal[i + 2]
            if i < n - 2
            else 0.0
        )

        y1 = (
            anticausal[i + 1]
            if i < n - 1
            else 0.0
        )

        y2 = (
            anticausal[i + 2]
            if i < n - 2
            else 0.0
        )

        anticausal[i] = (
            a3 * x1
            + a4 * x2
            + b1 * y1
            + b2 * y2
        )

    return causal + anticausal


# ============================================================
# Filtrado horizontal
# ============================================================

def filter_rows(image,coefficients) :

    height, width = image.shape

    result = np.zeros(
        (height, width),
        dtype=np.float32,
    )

    for y in range(height):

        result[y, :] = recursive_filter_1d(
            image[y, :],
            coefficients,
        )

    return result


# ============================================================
# Filtrado vertical
# ============================================================

def filter_columns(image,coefficients):

    height, width = image.shape

    result = np.zeros(
        (height, width),
        dtype=np.float32,
    )

    for x in range(width):

        result[:, x] = recursive_filter_1d(
            image[:, x],
            coefficients,
        )

    return result


# ============================================================
# Deriche X
# ============================================================

def deriche_x(image,coefficients) :

    # Derivada en X
    derivative_x = filter_rows(
        image,
        coefficients["derivative"],
    )

    # Suavizado en Y
    derivative_x = filter_columns(
        derivative_x,
        coefficients["smoothing"],
    )

    # Factor de escala de Deriche
    derivative_x *= (
        coefficients["derivative_scale"]
    )

    return derivative_x


# ============================================================
# Deriche Y
# ============================================================

def deriche_y(image,coefficients):

    # Derivada en Y
    derivative_y = filter_columns(
        image,
        coefficients["derivative"],
    )

    # Suavizado en X
    derivative_y = filter_rows(
        derivative_y,
        coefficients["smoothing"],
    )

    # Factor de escala de Deriche
    derivative_y *= (
        coefficients["derivative_scale"]
    )

    return derivative_y


# ============================================================
# Detector Deriche completo
# ============================================================

def deriche(image,alpha= 1.0):

    if image.ndim != 2:
        raise ValueError(
            "Deriche expects a grayscale 2D image."
        )

    image = np.asarray(
        image,
        dtype=np.float32,
    )

    coefficients = deriche_coefficients(
        alpha
    )

    gx = deriche_x(
        image,
        coefficients,
    )

    gy = deriche_y(
        image,
        coefficients,
    )

    magnitude = np.sqrt(
        gx ** 2 + gy ** 2
    )

    direction = np.arctan2(
        gy,
        gx,
    )

    return {
        "gx": gx,
        "gy": gy,
        "magnitude": magnitude,
        "direction": direction,
    }
