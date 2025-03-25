import cv2
import numpy as np

def harris_corner_detection(image: np.array, block_size: int = 2, ksize: int = 3) -> np.array:
    """
    Perform Harris corner detection on the input image.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).
        block_size (int): The size of the neighborhood considered for corner detection. Default is 2.
        ksize (int): The aperture parameter for the Sobel operator. Default is 3.

    Returns:
        np.array: The image with detected corners highlighted as a NumPy array.

    Raises:
        ValueError: If block_size or ksize is not a positive integer.
    """
    if block_size <= 0 or ksize <= 0:
        raise ValueError("block_size and ksize must be positive integers.")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Harris corner detector
    dst = cv2.cornerHarris(gray, block_size, ksize, 0.04)

    # Dilate the result to make the corners more visible
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    image[dst > 0.01 * dst.max()] = [0, 0, 255]

    return image