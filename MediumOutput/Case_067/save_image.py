import cv2
import numpy as np

def save_image(image: np.array, file_path: str) -> None:
    """
    Saves an image to a specified file path.

    Args:
        image (np.array): The input image to be saved.
        file_path (str): The file path where the image will be saved.

    Returns:
        None: The image is saved to disk.
    """
    cv2.imwrite(file_path, image)