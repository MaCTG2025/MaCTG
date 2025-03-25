import cv2
import numpy as np

def apply_adaptive_thresholding(gray_image: np.array, blockSize: int, C: int) -> np.array:
    """
    Apply adaptive thresholding to the grayscale image.

    Args:
        gray_image (np.array): The grayscale image as a NumPy array.
        blockSize (int): The size of the pixel neighborhood used to calculate the threshold value.
        C (int): A constant subtracted from the mean or weighted mean.

    Returns:
        np.array: The binary image obtained after adaptive thresholding.

    Raises:
        cv2.error: If the input image is not a single-channel (grayscale) image.
        ValueError: If blockSize is not an odd integer greater than 1.

    Requirements:
        - The input image must be a single-channel (grayscale) image.
        - blockSize must be an odd integer greater than 1.
        - C can be any integer, but typically small values (e.g., 2) are used.
    """
    if len(gray_image.shape) != 2:
        raise cv2.error("Input image must be a single-channel (grayscale) image.")
    
    if blockSize <= 1 or blockSize % 2 == 0:
        raise ValueError("blockSize must be an odd integer greater than 1.")

    return cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)