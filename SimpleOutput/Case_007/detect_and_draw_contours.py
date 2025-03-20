import cv2
import numpy as np

def detect_and_draw_contours(binary_image: np.array, output_path: str, color: tuple = (0, 0, 255), thickness: int = 2) -> np.array:
    """
    Detects contours in a binarized image, draws them in red with a specified thickness, and saves the resulting image.

    Args:
        binary_image (np.array): Binarized image as a NumPy array.
        ori_image (np.array): Original image as a NumPy array.
        output_path (str): Path to save the resulting image with contours.
        color (tuple, optional): RGB color for drawing contours (default is red).
        thickness (int, optional): Thickness of the contour lines (default is 2).

    Returns:
        np.array: Image with contours drawn as a NumPy array.
    """
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy of the binary image to draw contours on
    contours_image = binary_image.copy()

    # Convert the binary image to a 3-channel image
    contours_image = cv2.cvtColor(contours_image, cv2.COLOR_GRAY2BGR)

    # Draw contours on the copied image
    cv2.drawContours(contours_image, contours, -1, color, thickness)

    # Save the resulting image
    cv2.imwrite(output_path, contours_image)

    return contours_image