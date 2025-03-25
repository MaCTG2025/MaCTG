import cv2
import numpy as np

def apply_threshold(grayscale_image: np.array, threshold_value: int) -> np.array:
    """
    Apply a brightness threshold to separate bright and dark regions in the grayscale image.

    Args:
        grayscale_image (np.array): The grayscale image as a NumPy array with shape (height, width).
        threshold_value (int): The brightness threshold value (0-255).

    Returns:
        np.array: A binary mask as a NumPy array with shape (height, width), where bright regions are
                  represented by 1 (white) and dark regions by 0 (black).

    Requirements:
        - The input grayscale image must be a valid NumPy array.
        - The threshold_value must be an integer between 0 and 255.
        - The function should handle invalid threshold values gracefully.
    """
    # Check if the threshold value is within the valid range
    if not (0 <= threshold_value <= 255):
        raise ValueError("Threshold value must be between 0 and 255")

    # Apply the threshold using OpenCV's built-in function
    _, binary_mask = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Convert the binary mask from 0s and 255s to 0s and 1s
    binary_mask = binary_mask // 255

    return binary_mask