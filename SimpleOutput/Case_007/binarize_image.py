import cv2
import numpy as np

def binarize_image(grayscale_image: np.array, threshold: int = 128) -> np.array:
    """
    Binarizes a grayscale image using a specified threshold value.

    Args:
        grayscale_image (np.array): Grayscale image as a NumPy array.
        threshold (int, default=128): Threshold value for binarization.

    Returns:
        binary_image (np.array): Binarized image as a NumPy array.
    """
    # Apply binary thresholding
    _, binary_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)
    
    return binary_image