import cv2
import numpy as np

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Saves the resulting image to a file.

    Args:
        image (np.ndarray): The image to save as a NumPy array.
        output_path (str): The path where the image will be saved.

    Returns:
        None

    Requirements:
        - The function should save the image to the specified output path using OpenCV.
        - The image should be saved in PNG format.
    """
    cv2.imwrite(output_path, image)