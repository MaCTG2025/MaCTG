import cv2
import numpy as np

def load_image(image_path: str) -> np.array:
    """
    Load the input image from the specified file path.

    Args:
        image_path (str): The file path of the image to be loaded.

    Returns:
        np.array: The loaded image as a NumPy array with shape (height, width, channels).

    Requirements:
        - The image file must exist at the specified path.
        - The image must be in a format supported by OpenCV (e.g., PNG, JPEG).
        - The function should handle potential file I/O errors gracefully.
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Image not found or unable to read: {image_path}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None