import numpy as np 
from preparacion.generate_dataset import save_image
from pathlib import Path
OUTPUT_DIR = Path("synthetic_dataset")
GAUSSIAN_SIGMAS = [5, 10, 20, 30]
SALT_PEPPER_DENSITIES = [0.01, 0.05, 0.10]

SEED = 42
def add_gaussian_noise(image, sigma, rng):
    """
    Add zero-mean Gaussian noise with standard deviation sigma.

    The image remains uint8 and is clipped to [0, 255].
    """
    noise = rng.normal(loc=0.0,scale=sigma, size=image.shape,)
    noisy = image.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)
def add_salt_pepper_noise(image, density, rng):
    """
    Add salt-and-pepper noise.

    density = total percentage of corrupted pixels.
    Approximately half become 0 and half become 255.
    """
    noisy = image.copy()
    total_pixels = image.size
    number_corrupted = int(total_pixels * density)
    indices = rng.choice(total_pixels,size=number_corrupted,replace=False,)
    half = number_corrupted // 2
    flat = noisy.ravel()
    flat[indices[:half]] = 0
    flat[indices[half:]] = 255
    return noisy
def generate_variants(name, image, rng,output_dir):
    """
    Save clean image, ground truth, and all noisy variants.
    """
    directory = Path(output_dir) / name
    directory.mkdir(parents=True, exist_ok=True)

    # Gaussian noise
    for sigma in GAUSSIAN_SIGMAS:
        noisy = add_gaussian_noise(image,sigma,rng)
        save_image(directory / f"{name}_gaussian_sigma_{sigma}.jpg",noisy)
    # Salt-and-pepper noise
    for density in SALT_PEPPER_DENSITIES:
        percentage = int(density * 100)
        noisy = add_salt_pepper_noise(image,density,rng)
        save_image(directory / f"{name}_salt_pepper_{percentage}.jpg",noisy)
def noise_generation(names: list[str],images: list[np.ndarray],output_dir: str | Path):
    """
    Generate noisy variants for a dataset.

    Parameters
    ----------
    names:
        Image identifiers/names.

    images:
        Corresponding grayscale images.

    output_dir:
        Directory where the variants will be saved.
    """
    if len(names) != len(images):
        raise ValueError("names and images must have the same length.")
    rng = np.random.default_rng(SEED)
    for name, image in zip(names, images):
        generate_variants(name,image,rng,output_dir)
