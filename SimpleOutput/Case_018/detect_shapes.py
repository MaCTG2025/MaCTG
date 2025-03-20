import cv2
import numpy as np
from typing import List, Tuple, Dict

def detect_shapes(image_path: str) -> List[Tuple[np.array, str]]:
    """
    Detects shapes (rectangle, square, triangle, circle, star) in the input image and returns their contours and labels.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        List[Tuple[np.array, str]]: A list of tuples, where each tuple contains:
            - contour (np.array): The contour of the detected shape as a NumPy array.
            - shape_label (str): The label of the detected shape (e.g., 'rectangle', 'square', 'triangle', 'circle', 'star').
    """
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the image to get binary image
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize result list
    results = []

    # Loop through each contour
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Determine the number of vertices
        num_vertices = len(approx)

        # Classify the shape based on the number of vertices
        if num_vertices == 3:
            shape_label = 'triangle'
        elif num_vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                shape_label = 'square'
            else:
                shape_label = 'rectangle'
        elif num_vertices == 10:
            shape_label = 'star'
        elif num_vertices == 8:
            shape_label = 'circle'
        else:
            continue

        # Append the contour and label to the results list
        results.append((contour, shape_label))

    return results