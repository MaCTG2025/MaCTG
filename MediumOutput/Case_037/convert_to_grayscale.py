import cv2
import numpy as np

def convert_to_grayscale(image: np.array) -> np.array:
    """
    Convert the input image to grayscale.

    Args:
        image (np.array): The input image as a NumPy array.

    Returns:
        np.array: The grayscale version of the input image as a NumPy array.

    Raises:
        cv2.error: If the input image is not a valid 3-channel (BGR) or 1-channel (grayscale) image.

    Requirements:
        - The input image must be a valid 3-channel (BGR) or 1-channel (grayscale) image.
    """
    if len(image.shape) == 2:
        return image
    elif len(image.shape) == 3 and image.shape[2] == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        raise cv2.error("Input image must be a valid 3-channel (BGR) or 1-channel (grayscale) image.")