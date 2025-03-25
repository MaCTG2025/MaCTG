import numpy as np
import cv2

def apply_median_filter(image: np.ndarray, kernel_size: int) -> np.ndarray:
    """
    Applies median filtering to an input image with a specified kernel size.

    Args:
        image (np.ndarray): The input image as a NumPy array. It can be grayscale or color (3-channel).
        kernel_size (int): The size of the kernel for median filtering (e.g., 5 for a 5x5 kernel).

    Returns:
        np.ndarray: The filtered image as a NumPy array with the same shape as the input image.

    Requirements:
        - The input image must be a valid NumPy array.
        - The kernel size must be an odd integer greater than 1.
        - The function should handle both grayscale and color images.
    """
    # Check if the kernel size is valid
    if kernel_size <= 1 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd integer greater than 1.")

    # Apply median filter using OpenCV
    filtered_image = cv2.medianBlur(image, kernel_size)

    return filtered_image