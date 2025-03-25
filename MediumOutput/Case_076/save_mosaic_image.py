import numpy as np
from PIL import Image

def save_mosaic_image(mosaic_image: np.array, output_path: str) -> None:
    """
    Save the final mosaic image to a file.

    Args:
        mosaic_image (np.array): The mosaic image as a NumPy array.
        output_path (str): The file path where the mosaic image will be saved (e.g., "rotated_tiles.png").

    Returns:
        None

    Requirements:
        1. The mosaic image should be saved in the specified file path.
        2. The image format should match the file extension in `output_path` (e.g., PNG).
        3. The function should handle grayscale (2D) and RGB (3D) images.
    """
    # Convert the NumPy array to a PIL Image
    if len(mosaic_image.shape) == 2:
        pil_image = Image.fromarray((mosaic_image).astype(np.uint8), mode='L')
    elif len(mosaic_image.shape) == 3:
        pil_image = Image.fromarray((mosaic_image).astype(np.uint8))
    else:
        raise ValueError("Unsupported image shape")

    # Save the image to the specified file path
    pil_image.save(output_path)