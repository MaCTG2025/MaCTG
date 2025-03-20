import cv2
import numpy as np
from typing import List, Tuple, Dict

def draw_and_save_contours(image_path: str, shapes: List[Tuple[np.array, str]], colors: Dict[str, Tuple[int, int, int]], thickness: int, output_path: str) -> None:
    """
    Draws contours of detected shapes on the input image with specified colors and thickness, and saves the output image.

    Args:
        image_path (str): Path to the input image file.
        shapes (List[Tuple[np.array, str]]): A list of tuples, where each tuple contains:
            - contour (np.array): The contour of the detected shape as a NumPy array.
            - shape_label (str): The label of the detected shape (e.g., 'rectangle', 'square', 'triangle', 'circle', 'star').
        colors (Dict[str, Tuple[int, int, int]]): A dictionary mapping shape labels to contour colors as tuples of integers (BGR format).
        thickness (int): Thickness of the contour lines to be drawn.
        output_path (str): Path to save the output image file.

    Returns:
        None: The function saves the output image to the specified path.

    Requirements:
        - The function should use OpenCV to draw contours on the input image.
        - The function should apply the specified colors and thickness to the contours.
        - The function should save the resulting image to the specified output path.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Draw contours on the image
    for contour, shape_label in shapes:
        color = colors.get(shape_label, (0, 0, 0))  # Default to black if color not found
        cv2.drawContours(image, [contour], -1, color, thickness)

    # Save the output image
    cv2.imwrite(output_path, image)