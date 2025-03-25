import cv2
import numpy as np

def rotate_image(image: np.array) -> np.array:
    """
    Rotate the input image by 90 degrees clockwise.

    Args:
        image (np.array): The input image as a NumPy array.

    Returns:
        np.array: The rotated image as a NumPy array.

    Raises:
        ValueError: If the input is not a valid NumPy array.
    """
    if not isinstance(image, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")
    
    return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)