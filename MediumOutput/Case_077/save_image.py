import cv2
import numpy as np
import logging

def save_image(final_image: np.array, output_path: str) -> None:
    """
    Save the final image to the specified file path.

    Args:
        final_image (np.array): The final image as a NumPy array with shape (height, width).
        output_path (str): The file path where the final image will be saved.

    Returns:
        None

    Requirements:
        - The final_image must be a valid NumPy array.
        - The output_path must be a valid file path with a supported image format (e.g., PNG, JPEG).
        - The function should handle file I/O errors gracefully.
    """
    try:
        cv2.imwrite(output_path, final_image)
    except Exception as e:
        logging.error(f"Error saving image: {e}")