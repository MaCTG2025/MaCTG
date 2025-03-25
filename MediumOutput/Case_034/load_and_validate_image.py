import cv2
import numpy as np

def load_and_validate_image(image_path: str) -> np.array:
    """
    Load the input image from the specified file path and validate that it is a valid image.

    Args:
        image_path (str): The file path to the input image.

    Returns:
        np.array: The loaded image as a NumPy array.

    Raises:
        ValueError: If the image file does not exist at the specified path or is not a valid image.

    Notes:
        - The function uses OpenCV's `cv2.imread` to load the image.
        - The image is validated by checking if the returned array is not `None`.
        - The image is loaded in BGR format by default.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        raise ValueError("The file is not a valid image or cannot be read.")

    return image