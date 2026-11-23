from pathlib import Path
import cv2
import numpy as np

WIDTH= 481
HEIGHT=321 
OUTPUT_DIR = Path("synthetic_dataset")

SEED = 42
BACKGROUND = 0
FOREGROUND = 255
def create_canvas():
    """Create a black grayscale canvas."""
    return np.full((HEIGHT,WIDTH),BACKGROUND,dtype=np.uint8,)
def save_image(path, image):
    path.parent.mkdir(parents=True, exist_ok=True)
    success = cv2.imwrite(str(path), image)
    if not success:
        raise RuntimeError(f"Could not save image: {path}")
# ============================================================
# 1. BASIC GEOMETRY
# ============================================================
def generate_geometry():
    """
    Basic geometric structures:
        - rectangles
        - squares
        - circles
        - triangles
        - horizontal lines
        - vertical lines
        - diagonal lines
    """
    image = create_canvas()
    gt = create_canvas()
    # --------------------------------------------------------
    # Rectangles
    # --------------------------------------------------------
    cv2.rectangle( image,(int(0.08*WIDTH),int(0.15*HEIGHT)),(int(0.30*WIDTH),int(0.4*HEIGHT)),FOREGROUND,thickness=-1,)
    cv2.rectangle( image,(int(0.08*WIDTH),int(0.15*HEIGHT)),(int(0.30*WIDTH),int(0.4*HEIGHT)),FOREGROUND,thickness=-1,)
    # --------------------------------------------------------
    # Square
    # --------------------------------------------------------

    cv2.rectangle( image,(int(0.4*WIDTH),int(0.1*HEIGHT)),(int(0.60*WIDTH),int(0.35*HEIGHT)),FOREGROUND,thickness=-1,)
    cv2.rectangle( image,(int(0.4*WIDTH),int(0.1*HEIGHT)),(int(0.60*WIDTH),int(0.35*HEIGHT)),FOREGROUND,thickness=-1,)
    # --------------------------------------------------------
    # Circle
    # --------------------------------------------------------
    center = (int(0.82 * WIDTH), int(0.20 * HEIGHT),)
    radius = int(min(WIDTH, HEIGHT) * 0.18)
    cv2.circle(image,center,radius,FOREGROUND,thickness=-1,)
    cv2.circle(gt,center,radius,FOREGROUND,thickness=3,)

    # --------------------------------------------------------
    # Triangle
    # --------------------------------------------------------
    triangle = np.array(
        [
            [
                int(0.10 * WIDTH),
                int(0.55 * HEIGHT),
            ],
            [
                int(0.30 * WIDTH),
                int(0.90 * HEIGHT),
            ],
            [
                int(0.02 * WIDTH),
                int(0.90 * HEIGHT),
            ],
        ],
        dtype=np.int32,
    )
    cv2.fillPoly(image,[triangle],FOREGROUND,)
    cv2.polylines(gt,[triangle],isClosed=True,color=FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Hexagon
    # --------------------------------------------------------
    cx = int(0.57 * WIDTH)
    cy = int(0.65 * HEIGHT)
    r = int(min(WIDTH, HEIGHT) * 0.18)
    hexagon = np.array(
        [
            [
                cx - r,
                cy - r // 2,
            ],
            [
                cx,
                cy - r,
            ],
            [
                cx + r,
                cy - r // 2,
            ],
            [
                cx + r,
                cy + r // 2,
            ],
            [
                cx,
                cy + r,
            ],
            [
                cx - r,
                cy + r // 2,
            ],
        ],
        dtype=np.int32,
    )  
    cv2.fillPoly(image,[hexagon],FOREGROUND)
    cv2.polylines(gt,[hexagon],isClosed=True, color=FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Horizontal line
    # --------------------------------------------------------
    y = int(0.55 * HEIGHT)
    cv2.line(image,(int(0.72 * WIDTH), y),(int(0.97 * WIDTH), y),FOREGROUND,thickness=max(1, int(0.025 * HEIGHT)),)
    cv2.line(gt,(int(0.72 * WIDTH), y),(int(0.97 * WIDTH), y),FOREGROUND,thickness=3)
    # --------------------------------------------------------
    # Vertical line
    # --------------------------------------------------------
    x = int(0.80 * WIDTH)
    cv2.line(image,(x, int(0.65 * HEIGHT)),(x, int(0.95 * HEIGHT)),FOREGROUND,thickness=max(1, int(0.012 * WIDTH)),)
    cv2.line(gt,(x, int(0.65 * HEIGHT)),(x, int(0.95 * HEIGHT)),FOREGROUND,thickness=3,) 
    # --------------------------------------------------------
    # Diagonal lines
    # --------------------------------------------------------
    cv2.line(image,(int(0.08 * WIDTH), int(0.95 * HEIGHT)),(int(0.30 * WIDTH), int(0.78 * HEIGHT)),FOREGROUND,thickness=max(1, int(0.012 * HEIGHT)),)
    cv2.line(gt,(int(0.08 * WIDTH), int(0.95 * HEIGHT)),(int(0.30 * WIDTH), int(0.78 * HEIGHT)),FOREGROUND,thickness=3,)
    cv2.line(image,(int(0.35 * WIDTH), int(0.95 * HEIGHT)),(int(0.60 * WIDTH), int(0.75 * HEIGHT)),FOREGROUND,thickness=max(1, int(0.025 * HEIGHT)),)
    cv2.line(gt,(int(0.35 * WIDTH), int(0.95 * HEIGHT)),(int(0.60 * WIDTH), int(0.75 * HEIGHT)),FOREGROUND,thickness=3,)
    return image, gt

# ============================================================
# 2. ORIENTATION
# ============================================================
def generate_orientation():
    """
    Lines with controlled orientations and thicknesses.
    """
    image = create_canvas()
    gt = create_canvas()
    angles = [0, 15, 30, 45, 60, 75, 90]
    thicknesses = [1, 2, 4, 8]
    # Four rows of different thicknesses.
    y_positions = np.linspace(0.12*HEIGHT,0.88*HEIGHT,len(thicknesses))
    length = int(0.25*min(WIDTH,HEIGHT))
    for row, thickness in enumerate(thicknesses):
        cy =int( y_positions[row])
        for i, angle in enumerate(angles):
            cx = int((i+0.5)*WIDTH/len(angles))
            theta = np.deg2rad(angle)
            dx = int(length * np.cos(theta))
            dy = int(length * np.sin(theta))
            p1 = (cx - dx // 2, cy - dy // 2,)
            p2 = (cx + dx // 2,cy + dy // 2,)
            cv2.line(image,p1,p2,FOREGROUND,thickness=thickness,)
            # Ground truth represents the center/localization
            # of the ideal edge.
            cv2.line(gt,p1,p2,FOREGROUND,thickness=3,)
    return image, gt

# ============================================================
# 3. CORNERS AND CLOSE STRUCTURES
# ============================================================
def generate_corners():
    """
    Tests:
        - corners
        - intersections
        - acute angles
        - parallel lines
        - closely spaced structures
    """
    image = create_canvas()
    gt = create_canvas()
    # --------------------------------------------------------
    # 90-degree corner
    # --------------------------------------------------------
    x1 = int(0.10 * WIDTH)
    y1 = int(0.25 * HEIGHT)
    x2 = int(0.35 * WIDTH)
    y2 = int(0.75 * HEIGHT)
    cv2.line(image,(x1, y1),(x2, y1),FOREGROUND,thickness=8,)
    cv2.line(image,(x1, y1),(x1, y2),FOREGROUND,thickness=8,)
    cv2.line(gt,(x1, y1),(x2, y1),FOREGROUND,thickness=3,)
    cv2.line(gt,(x1, y1),(x1, y2),FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Acute corner
    # --------------------------------------------------------
    p1 = (int(0.40 * WIDTH),int(0.70 * HEIGHT),)
    p2 = (int(0.60 * WIDTH),int(0.25 * HEIGHT),)
    p3 = (int(0.80 * WIDTH),int(0.70 * HEIGHT),)
    cv2.line(image,p1,p2,FOREGROUND,thickness=8,)
    cv2.line(image,p2,p3,FOREGROUND,thickness=8,)
    cv2.line(gt,p1,p2,FOREGROUND,thickness=3,)
    cv2.line(gt,p2,p3,FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Intersection
    # --------------------------------------------------------
    cv2.line(image,(int(0.10 * WIDTH), int(0.75 * HEIGHT)),(int(0.35 * WIDTH), int(0.95 * HEIGHT)),FOREGROUND,thickness=8,)
    cv2.line(image,(int(0.10 * WIDTH), int(0.95 * HEIGHT)),(int(0.35 * WIDTH), int(0.75 * HEIGHT)),FOREGROUND,thickness=8,)
    cv2.line(gt,(int(0.10 * WIDTH), int(0.75 * HEIGHT)),(int(0.35 * WIDTH), int(0.95 * HEIGHT)),FOREGROUND,thickness=3,)
    cv2.line(gt,(int(0.10 * WIDTH), int(0.95 * HEIGHT)),(int(0.35 * WIDTH), int(0.75 * HEIGHT)),FOREGROUND,thickness=3,) 
    # --------------------------------------------------------
    # Parallel lines with decreasing separation
    # --------------------------------------------------------
    separations = [32, 16, 8, 4]
    x_start = int(0.6*WIDTH)
    x_end = int(0.97*WIDTH)
    base_y = int(0.6*HEIGHT)
    for i, separation in enumerate(separations):
        y1 = base_y + i * int(0.07*HEIGHT)
        y2 = y1 + separation
        if y2 >=HEIGHT:
            continue
        cv2.line(image,(x_start, y1),(x_end, y1),FOREGROUND,thickness=3,)
        cv2.line(image,(x_start, y2),(x_end, y2),FOREGROUND,thickness=3,)
        cv2.line(gt,(x_start, y1),(x_end, y1),FOREGROUND,thickness=3,)
        cv2.line(gt,(x_start, y2),(x_end, y2),FOREGROUND,thickness=3,)
    return image, gt
# ============================================================
# 4. CURVES
# ============================================================

def generate_curves():
    """
    Curves, circles, ellipses and sinusoidal structures.
    """
    image = create_canvas()
    gt = create_canvas()
    # --------------------------------------------------------
    # Concentric circles
    # --------------------------------------------------------
    center = (int(0.25*WIDTH),int(0.30*HEIGHT))
    max_radius=int(min(WIDTH,HEIGHT)*0.25)
    for radius in [int(max_radius*0.33),int(max_radius*0.66),max_radius]:
        cv2.circle(image,center,radius,FOREGROUND,thickness=6,)
        cv2.circle(gt,center,radius,FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Ellipses
    # --------------------------------------------------------
    cv2.ellipse(image,(int(0.70 * WIDTH),int(0.30 * HEIGHT),),(int(0.35 * WIDTH),int(0.25 * HEIGHT),),20,0,360,FOREGROUND,thickness=6,)
    cv2.ellipse(gt,(int(0.70 * WIDTH),int(0.30 * HEIGHT),),(int(0.35 * WIDTH),int(0.25 * HEIGHT),),20,0,360,FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Arcs
    # --------------------------------------------------------
    cv2.ellipse(image,(int(0.25 * WIDTH),int(0.75 * HEIGHT),),(int(0.35 * WIDTH),int(0.30 * HEIGHT),),0,20,150,FOREGROUND,thickness=8,)
    cv2.ellipse(gt,(int(0.25 * WIDTH),int(0.75 * HEIGHT),),(int(0.35 * WIDTH),int(0.30 * HEIGHT),),0,20,150,FOREGROUND,thickness=3,)
    # --------------------------------------------------------
    # Sinusoidal curve
    # --------------------------------------------------------
    points = []
    x_start = int(0.45 * WIDTH)
    x_end = int(0.98 * WIDTH)
    amplitude = int( 0.15 * HEIGHT)
    center_y = int(0.72 * HEIGHT)
    period = int(0.45 * WIDTH)
    for x in range(x_start,x_end):
        y = int(center_y+ amplitude* np.sin(2* np.pi* (x - x_start)/ period))
        if 0 <= y < HEIGHT:
            points.append([x, y])
    points = np.array(points,dtype=np.int32,)
    cv2.polylines(image,[points],False,FOREGROUND,thickness=6,)
    cv2.polylines(gt,[points],False,FOREGROUND,thickness=3,)
    return image, gt
# ============================================================
# 5. SPATIAL FREQUENCY
# ============================================================
def generate_frequency():
    """
    Increasing spatial frequency.

    The image contains groups of parallel lines whose
    separation decreases progressively.
    """
    image = create_canvas()
    gt = create_canvas()
    separations = [32, 16, 8, 4, 2, 1]
    x_start = int(0.10 * WIDTH)
    x_end = int(0.90 * WIDTH)
    region_height =  HEIGHT//6 
    for region, separation in enumerate(separations):
        y_start = region * region_height
        y_end = y_start + region_height
        x = x_start
        while x <= x_end:
            cv2.line(image,(x, y_start),(x, y_end),FOREGROUND,thickness=1,)
            cv2.line(gt,(x, y_start),(x, y_end),FOREGROUND,thickness=1,)
            x += separation
    # --------------------------------------------------------
    # Concentric circles in lower area
    # --------------------------------------------------------
    center = (int(0.75 * WIDTH),int(0.85 * HEIGHT),)
    max_radius=int(min(WIDTH,HEIGHT)*0.4)
    for radius in range(10,max_radius,10):
        cv2.circle(image,center,radius,FOREGROUND,thickness=1,)
        cv2.circle(gt,center,radius,FOREGROUND,thickness=1,)
    return image, gt
# ============================================================
# DATASET GENERATION
# ============================================================
def main_p():
    rng = np.random.default_rng(SEED)
    generators = {
        "geometry": generate_geometry,
        "orientation": generate_orientation,
        "corners": generate_corners,
        "curves": generate_curves,
        "frequency": generate_frequency,
    }
    for name, generator in generators.items():
        print(f"Generating: {name}")
        image, ground_truth = generator()
        directory = OUTPUT_DIR / name
        directory.mkdir(parents=True, exist_ok=True)
        save_image(directory / "clean.jpg", image)
        save_image(directory / "ground_truth.jpg", ground_truth)

    print()
    print("Dataset generated successfully.")
    print(f"Output: {OUTPUT_DIR.resolve()}")

