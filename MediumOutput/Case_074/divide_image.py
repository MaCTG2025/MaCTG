from typing import List
import numpy as np
from PIL import Image

def divide_image(image: np.ndarray) -> List[np.ndarray]:
    """
    Divides the input image into four equal regions.

    Args:
        image (np.ndarray): The input image as a NumPy array. The image should be in RGB format.

    Returns:
        List[np.ndarray]: A list of four NumPy arrays, each representing one of the four equal regions of the image.
                          The regions are ordered as [top-left, top-right, bottom-left, bottom-right].
    """
    height, width = image.shape[:2]
    
    if height % 2 != 0 or width % 2 != 0:
        raise ValueError("Image dimensions must be divisible by 2.")
    
    top_left = image[:height//2, :width//2]
    top_right = image[:height//2, width//2:]
    bottom_left = image[height//2:, :width//2]
    bottom_right = image[height//2:, width//2:]
    
    return [top_left, top_right, bottom_left, bottom_right]