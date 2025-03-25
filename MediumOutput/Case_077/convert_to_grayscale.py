import cv2
import numpy as np

def convert_to_grayscale(image: np.array) -> np.array:
    """
    Convert the input image to grayscale.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).

    Returns:
        np.array: The grayscale image as a NumPy array with shape (height, width).

    Requirements:
        - The input image must be a valid NumPy array with 3 channels (RGB).
        - The function should handle grayscale conversion errors gracefully.
    """
    try:
        if image.shape[2] != 3:
            raise ValueError("Input image must have 3 channels (RGB).")
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return grayscale_image
    except Exception as e:
        print(f"Error converting to grayscale: {e}")
        return None