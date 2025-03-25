import cv2
import numpy as np

def divide_into_quadrants(grayscale_image: np.array) -> dict:
    """
    Divides the grayscale image into four quadrants.

    Args:
        grayscale_image (np.array): Grayscale image as a NumPy array.

    Returns:
        dict: A dictionary containing four quadrants:
            - top_left (np.array): Top-left quadrant of the image.
            - top_right (np.array): Top-right quadrant of the image.
            - bottom_left (np.array): Bottom-left quadrant of the image.
            - bottom_right (np.array): Bottom-right quadrant of the image.

    Requirements:
        - The input image must be a grayscale image (2D NumPy array).
        - The image is divided into four equal parts based on its height and width.
    """
    height, width = grayscale_image.shape
    top_left = grayscale_image[:height//2, :width//2]
    top_right = grayscale_image[:height//2, width//2:]
    bottom_left = grayscale_image[height//2:, :width//2]
    bottom_right = grayscale_image[height//2:, width//2:]

    return {
        'top_left': top_left,
        'top_right': top_right,
        'bottom_left': bottom_left,
        'bottom_right': bottom_right
    }