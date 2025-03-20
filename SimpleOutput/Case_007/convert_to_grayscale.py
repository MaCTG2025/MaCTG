import cv2
import numpy as np

def convert_to_grayscale(image_path: str) -> np.array:
    """
    Converts an input image to grayscale.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        np.array: Grayscale image as a NumPy array.
    """
    # Read the image from the specified file path
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return grayscale_image