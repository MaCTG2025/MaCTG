import cv2
import numpy as np

def transform_object_image(object_image: np.ndarray) -> np.ndarray:
    """
    Downscale the object image by 0.5x and rotate it by 45 degrees.

    Args:
        object_image (np.ndarray): The object image as a NumPy array.

    Returns:
        np.ndarray: The transformed object image as a NumPy array.

    Requirements:
        - The downscaling should maintain the aspect ratio of the object image.
        - The rotation should be performed around the center of the image.
        - The function should handle edge cases (e.g., empty input) gracefully.
    """
    if object_image is None or len(object_image.shape) == 0:
        return np.array([])

    # Check if the image has more than one pixel
    if object_image.shape[0] <= 1 or object_image.shape[1] <= 1:
        return object_image

    # Downscale the image by 0.5x while maintaining the aspect ratio
    scaled_image = cv2.resize(object_image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    # Rotate the image by 45 degrees around its center
    rows, cols = scaled_image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    return cv2.warpAffine(scaled_image, M, (cols, rows))