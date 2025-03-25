import cv2
import numpy as np

def save_image(image: np.array, output_path: str) -> None:
    """
    Save the input image to the specified file path.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).
        output_path (str): The file path where the image will be saved.

    Returns:
        None

    Requirements:
        - The input image must be a valid NumPy array.
        - The output path must be writable.
        - The image should be saved in the specified format (e.g., PNG).

    Example:
        >>> save_image(image, "output_image.png")
    """
    cv2.imwrite(output_path, image)