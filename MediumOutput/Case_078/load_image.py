import cv2
import numpy as np
from typing import Optional

def load_image(image_path: str) -> Optional[np.array]:
    """
    Load the input image from the specified file path.

    Args:
        image_path (str): The file path to the input image.

    Returns:
        np.array: The loaded image as a NumPy array, or None if an error occurs.

    Raises:
        FileNotFoundError: If the image file does not exist at the specified path.
        ValueError: If the image format is not supported by OpenCV.
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Unsupported image format for file: {image_path}")
        return image
    except FileNotFoundError:
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")