import cv2
import numpy as np
from typing import Optional

def divide_image_and_apply_flood_fill(image_path: str, threshold: int = 30) -> np.array:
    """
    Divides the image into four fixed regions (top-left, top-right, bottom-left, bottom-right), 
    applies flood fill starting from the center of each region based on gradient similarity, 
    and highlights each region with a specific color.

    Parameters:
        image_path (str): Path to the input image file.
        threshold (int, optional): Gradient similarity threshold for flood fill. Default is 30.

    Returns:
        segmented_image (np.array): A NumPy array representing the segmented image with regions 
        highlighted in red, green, blue, and yellow.
    """
    # Check if the image can be loaded
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image at {image_path} does not exist.")
    
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load the image at {image_path}.")
    
    height, width = image.shape[:2]
    
    # Define the regions
    top_left_region = image[0:height//2, 0:width//2]
    top_right_region = image[0:height//2, width//2:]
    bottom_left_region = image[height//2:, 0:width//2]
    bottom_right_region = image[height//2:, width//2:]
    
    # Create a copy of the original image to draw on
    segmented_image = image.copy()
    
    # Function to apply flood fill
    def apply_flood_fill(region, center, color):
        mask = np.zeros_like(region, dtype=np.uint8)
        cv2.floodFill(region, mask, center, color, loDiff=(threshold,)*region.ndim, upDiff=(threshold,)*region.ndim)
        return region
    
    # Apply flood fill to each region
    top_left_center = (width//4, height//4)
    top_right_center = (3*width//4, height//4)
    bottom_left_center = (width//4, 3*height//4)
    bottom_right_center = (3*width//4, 3*height//4)
    
    top_left_color = (0, 0, 255)  # Red
    top_right_color = (0, 255, 0)  # Green
    bottom_left_color = (255, 0, 0)  # Blue
    bottom_right_color = (0, 255, 255)  # Yellow
    
    segmented_image[0:height//2, 0:width//2] = apply_flood_fill(top_left_region, top_left_center, top_left_color)
    segmented_image[0:height//2, width//2:] = apply_flood_fill(top_right_region, top_right_center, top_right_color)
    segmented_image[height//2:, 0:width//2] = apply_flood_fill(bottom_left_region, bottom_left_center, bottom_left_color)
    segmented_image[height//2:, width//2:] = apply_flood_fill(bottom_right_region, bottom_right_center, bottom_right_color)
    
    return segmented_image