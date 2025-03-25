import cv2
import numpy as np
import os

def draw_rectangle_and_save(brightened_image: np.array, matched_region: tuple, output_path: str) -> None:
    """
    Draws a rectangle around the matched region and saves the resulting image.

    Args:
        brightened_image (np.array): A NumPy array representing the brightened image.
        matched_region (tuple): A tuple (x, y, w, h) representing the matched region's
                                top-left corner coordinates (x, y), width (w), and height (h).
        output_path (str): Path to save the resulting image (e.g., "wheres_waldo_matched.png").

    Returns:
        None: The function saves the image to disk and does not return anything.

    Raises:
        FileNotFoundError: If the output directory does not exist.
    """
    # Check if the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        raise FileNotFoundError(f"Output directory does not exist: {output_dir}")

    x, y, w, h = matched_region
    cv2.rectangle(brightened_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imwrite(output_path, brightened_image)