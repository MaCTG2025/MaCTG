import cv2
import numpy as np

def detect_and_draw_contours(binary_image: np.array, color: tuple, thickness: int) -> np.array:
    """
    Detect contours in the binary image and draw them in red with a specified thickness.

    Args:
        binary_image (np.array): The binary image as a NumPy array.
        color (tuple): The color of the contours in BGR format (e.g., (0, 0, 255) for red).
        thickness (int): The thickness of the contour lines.

    Returns:
        np.array: The output image with contours drawn on it.

    Raises:
        cv2.error: If the input image is not a binary image (black and white).
        ValueError: If the color is not a tuple of three integers representing BGR values.
        ValueError: If the thickness is not a positive integer.

    Requirements:
        - The input image must be a binary image (black and white).
        - The color must be a tuple of three integers representing BGR values.
        - The thickness must be a positive integer.
    """
    # Check if the color is a tuple of three integers
    if not isinstance(color, tuple) or len(color) != 3 or not all(isinstance(c, int) for c in color):
        raise ValueError("Color must be a tuple of three integers representing BGR values.")

    # Check if the thickness is a positive integer
    if not isinstance(thickness, int) or thickness <= 0:
        raise ValueError("Thickness must be a positive integer.")

    # Check if the input image is a binary image
    if len(np.unique(binary_image)) != 2:
        raise cv2.error("Input image must be a binary image.")

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    output_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_image, contours, -1, color, thickness)

    return output_image