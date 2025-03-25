import cv2
import numpy as np

def combine_quadrants(processed_quadrants: dict) -> np.array:
    """
    Combines the processed quadrants back into a single image.

    Args:
        processed_quadrants (dict): Dictionary containing the processed quadrants.

    Returns:
        np.array: Combined image as a NumPy array.

    Requirements:
        - The input quadrants must be of the same size and type.
        - The function concatenates the quadrants back into their original positions.
    """
    # Assuming the dictionary keys are 'top_left', 'top_right', 'bottom_left', 'bottom_right'
    top_left = processed_quadrants['top_left']
    top_right = processed_quadrants['top_right']
    bottom_left = processed_quadrants['bottom_left']
    bottom_right = processed_quadrants['bottom_right']

    # Get the height and width of one quadrant
    height, width = top_left.shape[:2]

    # Create an empty image with double the height and width of one quadrant
    combined_image = np.zeros((height * 2, width * 2), dtype=top_left.dtype)

    # Paste each quadrant into its correct position
    combined_image[0:height, 0:width] = top_left
    combined_image[0:height, width:width*2] = top_right
    combined_image[height:height*2, 0:width] = bottom_left
    combined_image[height:height*2, width:width*2] = bottom_right

    return combined_image