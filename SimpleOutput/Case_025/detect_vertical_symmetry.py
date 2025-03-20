import cv2
import numpy as np
from typing import Optional, Tuple

def detect_vertical_symmetry(image_path: str) -> Tuple[Optional[int], np.ndarray]:
    """
    Analyzes an input image to detect vertical symmetry.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        Tuple[Optional[int], np.ndarray]: A tuple containing:
            - axis_x (int or None): The x-coordinate of the vertical symmetry axis. 
              Returns None if no symmetry is detected.
            - image (np.ndarray): The loaded image as a NumPy array.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError("Image not found at the specified path.")
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the horizontal flip of the image
    flipped_image = cv2.flip(gray_image, 1)
    
    # Compute the absolute difference between the original and flipped images
    diff_image = cv2.absdiff(gray_image, flipped_image)
    
    # Threshold the difference image to create a binary mask
    _, thresholded_diff = cv2.threshold(diff_image, 10, 255, cv2.THRESH_BINARY)
    
    # Find contours in the thresholded difference image
    contours, _ = cv2.findContours(thresholded_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check if there are any contours
    if len(contours) == 0:
        return None, image
    
    # Calculate the average position of the contours
    total_contour_length = sum(cv2.arcLength(cnt, True) for cnt in contours)
    avg_contour_position = sum(np.mean(cnt[:, :, 0]) for cnt in contours) / len(contours)
    
    # Calculate the x-coordinate of the vertical symmetry axis
    axis_x = int(avg_contour_position)
    
    # Check if the symmetry axis falls within the image width
    if 0 <= axis_x < image.shape[1]:
        return axis_x, image
    else:
        return None, image