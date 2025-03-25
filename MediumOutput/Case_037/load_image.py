import cv2
import numpy as np

def load_image(image_path: str) -> np.array:
    """
    Load the input image from the specified file path.

    Args:
        image_path (str): The file path of the image to be loaded.

    Returns:
        np.array: The loaded image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file does not exist at the specified path.
        cv2.error: If the image format is not supported by OpenCV.

    Requirements:
        - The image file must exist at the specified path.
        - The image must be in a format supported by OpenCV (e.g., PNG, JPEG).
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
        return image
    except cv2.error as e:
        raise cv2.error(f"Error loading the image: {e}")