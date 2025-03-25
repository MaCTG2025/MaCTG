import cv2
import numpy as np

def rotate_image(image_path: str) -> np.array:
    """
    Rotates the input image by 180 degrees.

    Args:
        image_path (str): The file path to the input image.

    Returns:
        np.array: The rotated image as a NumPy array.

    Raises:
        ValueError: If the image cannot be read from the specified path.

    Example:
        rotated_image = rotate_image("./test_image.png")
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to read.")
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)
        return rotated_image
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")