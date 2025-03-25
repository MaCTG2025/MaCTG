import cv2
import numpy as np

def apply_bilateral_filter(image_path: str, d: int, sigmaColor: float, sigmaSpace: float) -> np.array:
    """
    Applies bilateral filtering to the input image to reduce noise while preserving edges.

    Args:
        image_path (str): Path to the input image file.
        d (int): Diameter of each pixel neighborhood used during filtering.
        sigmaColor (float): Filter sigma in the color space. A larger value means that farther colors 
                            within the pixel neighborhood will be mixed together.
        sigmaSpace (float): Filter sigma in the coordinate space. A larger value means that farther 
                            pixels will influence each other as long as their colors are close enough.

    Returns:
        np.array: The filtered image as a NumPy array.
    """
    # Read the image from the given path
    image = cv2.imread(image_path)
    
    # Check if the image is loaded properly
    if image is None:
        raise ValueError("Image not found at the specified path.")
    
    # Apply bilateral filter
    filtered_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    
    return filtered_image
