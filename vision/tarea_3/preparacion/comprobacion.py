from pathlib import Path
import pandas as pd
from PIL import Image
IMAGE_EXTENSIONS = {".jpg",".jpeg", ".png",".bmp",".tif",".tiff",".webp",}
def report(root: str | Path,output_csv: str | Path | None = None,output_tex: str | Path | None = None,) -> pd.DataFrame:
    """
    Recursively inspect all images inside `root`.
    Parameters
    ----------
    root:
        Root directory to inspect.

    output_csv:
        Optional path where the DataFrame will be saved as CSV.

    output_tex:
        Optional path where the DataFrame will be saved as LaTeX.

    Returns
    -------
    pd.DataFrame
        DataFrame containing image metadata.
    """
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {root}")
    records = []
    # Recursively find images
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        try:
            with Image.open(path) as img:
                width, height = img.size
                record = {
                    "root":str(root),
                    "filename": path.name,
                    "relative_path": str(path.relative_to(root)),
                    "directory": (str(path.parent.relative_to(root)) if path.parent != root else "."),
                    "width": width,
                    "height": height,
                    "channels": len(img.getbands()),
                    "mode": img.mode,
                    "aspect_ratio": width / height,
                }
                records.append(record)
        except Exception as exc:
            print(f"Could not read {path}: {exc}")
    # Create DataFrame
    df = pd.DataFrame(records)
    if df.empty:
        print(f"No images found in: {root}")
        return df
    # Sort
    df = df.sort_values(by=["directory", "filename"]).reset_index(drop=True)
    # Optional CSV
    if output_csv is not None:
        output_csv = Path(output_csv)
        output_csv.parent.mkdir(parents=True,exist_ok=True,)
        df.to_csv(output_csv,index=False)
        print(f"CSV saved to: {output_csv}")
    # Optional LaTeX
    if output_tex is not None:
        output_tex = Path(output_tex)
        output_tex.parent.mkdir(parents=True,exist_ok=True,)
        latex = df.to_latex(index=False,float_format=lambda x: f"{x:.3f}",escape=True,)
        output_tex.write_text(latex,encoding="utf-8",)
        print(f"LaTeX saved to: {output_tex}")
    return df
