import os
import cv2
import numpy as np

def convert_to_grayscale(image_path: str) -> np.array:
    """
    Converts the input image to grayscale.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        np.array: Grayscale image as a NumPy array.
    """
    # Check if the file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Check if the image was successfully read
    if image is None:
        raise cv2.error(f"Could not read the image at {image_path}.")
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return grayscale_image