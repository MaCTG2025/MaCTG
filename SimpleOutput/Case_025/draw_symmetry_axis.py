import cv2
import numpy as np
from typing import Optional

def draw_symmetry_axis(image: np.ndarray, axis_x: Optional[int]) -> np.ndarray:
    """
    Draws a vertical green line along the symmetry axis (if detected) on the input image.

    Args:
        image (np.ndarray): The input image as a NumPy array.
        axis_x (int or None): The x-coordinate of the vertical symmetry axis. 
            If None, no line is drawn.

    Returns:
        np.ndarray: The image with a vertical green line drawn along the symmetry axis (if detected).
    """
    if axis_x is not None:
        cv2.line(image, (axis_x, 0), (axis_x, image.shape[0]), (0, 255, 0), 2)
    return image