import cv2
import numpy as np

def perform_template_matching(brightened_image: np.array, template_path: str) -> tuple:
    """
    Performs template matching on the brightened image using the provided template.

    Args:
        brightened_image (np.array): A NumPy array representing the brightened image.
        template_path (str): Path to the template image file (e.g., "./waldo.jpg").

    Returns:
        tuple: A tuple (x, y, w, h) representing the matched region's top-left corner
               coordinates (x, y), width (w), and height (h).
    """
    # Load the template image
    template = cv2.imread(template_path, 0)
    
    # Get dimensions of the template
    template_height, template_width = template.shape
    
    # Perform template matching
    result = cv2.matchTemplate(brightened_image, template, cv2.TM_CCOEFF_NORMED)
    
    # Find the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Extract the top-left corner coordinates and dimensions of the matched region
    x, y = max_loc
    w, h = template_width, template_height
    
    return (x, y, w, h)