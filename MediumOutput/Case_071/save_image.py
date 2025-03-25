import os
import cv2
import numpy as np

def save_image(result_image: np.ndarray, output_path: str) -> None:
    """
    Save the final blended image to a file.

    Args:
        result_image (np.ndarray): The final blended image as a NumPy array.
        output_path (str): The file path where the image will be saved.

    Returns:
        None

    Requirements:
        - The image should be saved in a format supported by OpenCV (e.g., JPEG, PNG).
        - The function should handle file path errors gracefully and raise appropriate exceptions.
    """
    try:
        cv2.imwrite(output_path, result_image)
    except Exception as e:
        raise IOError(f"Failed to save image to {output_path}: {e}")