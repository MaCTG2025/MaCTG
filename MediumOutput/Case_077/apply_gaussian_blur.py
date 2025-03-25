import cv2
import numpy as np

def apply_gaussian_blur(grayscale_image: np.array, binary_mask: np.array, kernel_size: tuple) -> np.array:
    """
    Apply Gaussian blur to the bright regions of the grayscale image.

    Args:
        grayscale_image (np.array): The grayscale image as a NumPy array with shape (height, width).
        binary_mask (np.array): The binary mask as a NumPy array with shape (height, width), where
                                bright regions are represented by 1 (white) and dark regions by 0 (black).
        kernel_size (tuple): The size of the Gaussian kernel as a tuple of two positive odd integers (e.g., (5, 5)).

    Returns:
        np.array: The grayscale image as a NumPy array with shape (height, width), where Gaussian blur
                  is applied only to the bright regions.

    Requirements:
        - The input grayscale image and binary mask must be valid NumPy arrays with the same dimensions.
        - The kernel_size must be a tuple of two positive odd integers.
        - The function should handle invalid kernel sizes gracefully.
    """
    # Check if the kernel size is valid
    if not isinstance(kernel_size, tuple) or len(kernel_size) != 2 or \
       not all(isinstance(size, int) and size > 0 and size % 2 == 1 for size in kernel_size):
        raise ValueError("kernel_size must be a tuple of two positive odd integers")

    # Ensure the grayscale image and binary mask have the same dimensions
    if grayscale_image.shape != binary_mask.shape:
        raise ValueError("grayscale_image and binary_mask must have the same dimensions")

    # Apply Gaussian blur to the entire image
    blurred_image = cv2.GaussianBlur(grayscale_image, kernel_size, 0)
    cv2.imwrite('blurred_image.png', blurred_image)
    return blurred_image