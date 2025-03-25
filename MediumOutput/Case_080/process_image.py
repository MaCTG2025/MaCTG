import numpy as np
import cv2
import os

def process_image(image_path: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Converts the input image to grayscale, applies histogram equalization, and returns the grayscale image,
    equalized image, original histogram, and equalized histogram.

    Args:
        image_path (str): Path to the input image file. The image must be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: A tuple containing the grayscale image, equalized image,
        original histogram, and equalized histogram.
    """
    # Read the image from the provided file path
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)

    # Compute the original histogram
    original_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Compute the equalized histogram
    equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    return gray_image, equalized_image, original_hist, equalized_hist
