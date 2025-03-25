import cv2
import numpy as np

def compute_gradient_magnitude(image: np.array) -> np.array:
    """
    Compute the gradient magnitude of an image using the Sobel operator with a kernel size of 5.

    Args:
        image (np.array): The input image as a NumPy array.

    Returns:
        np.array: The gradient magnitude of the image as a NumPy array.

    Raises:
        ValueError: If the input is not a valid NumPy array.
    """
    if not isinstance(image, np.ndarray):
        raise ValueError("Input must be a valid NumPy array.")

    # Apply Sobel operator in x and y direction
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

    # Compute gradient magnitude
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)

    return gradient_magnitude