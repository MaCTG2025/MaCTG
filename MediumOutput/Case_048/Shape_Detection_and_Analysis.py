import cv2
import numpy as np
from detect_shapes_and_compute_metrics import detect_shapes_and_compute_metrics

def shape_detection_and_analysis(image_path: str) -> None:
    """
    Detects shapes in the given image, computes their areas and perimeters, and saves the results into a .npy file.

    Args:
        image_path (str): The file path to the input image (e.g., "./shapes_r.png").

    Returns:
        None: The function does not return any value. It saves the computed areas and perimeters into a file
              named "areas_perimeters.npy".
    """
    detect_shapes_and_compute_metrics(image_path)