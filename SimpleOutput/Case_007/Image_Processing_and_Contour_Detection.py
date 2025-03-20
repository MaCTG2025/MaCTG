from convert_to_grayscale import convert_to_grayscale
from binarize_image import binarize_image
from detect_and_draw_contours import detect_and_draw_contours
import numpy as np

def process_image_and_detect_contours(image_path: str, output_path: str, threshold: int = 128) -> np.ndarray:
    """
    Processes an input image by converting it to grayscale, binarizing it, detecting contours, and saving the result.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the resulting image with contours.
        threshold (int, default=128): Threshold value for binarization.

    Returns:
        np.ndarray: Image with contours drawn as a NumPy array.
    """
    grayscale_image = convert_to_grayscale(image_path)
    binary_image = binarize_image(grayscale_image, threshold)
    contours_image = detect_and_draw_contours(binary_image, output_path)
    return contours_image