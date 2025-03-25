import cv2
import numpy as np

def load_image(image_path: str) -> np.array:
    """
    Load the input image from the specified file path.

    Args:
        image_path (str): The file path of the image to be loaded.

    Returns:
        np.array: The loaded image as a NumPy array with shape (height, width, channels).

    Raises:
        FileNotFoundError: If the image file does not exist at the specified path.

    Example:
        >>> image = load_image("./test_image.png")
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"The image file {image_path} could not be found.")
        return image
    except Exception as e:
        raise e