import cv2
import numpy as np

def save_image(processed_image: np.array, output_path: str) -> None:
    """
    Saves the processed image to a file.

    Args:
        processed_image (np.array): Processed image as a NumPy array.
        output_path (str): Path to save the processed image.

    Returns:
        None: The image is saved to disk.
    """
    cv2.imwrite(output_path, processed_image)