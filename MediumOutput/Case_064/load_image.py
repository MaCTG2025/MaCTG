from PIL import Image
import numpy as np

def load_image(image_path: str) -> np.array:
    """
    Load an image from the specified file path and return it as a NumPy array.

    Args:
        image_path (str): The path to the image file (e.g., "./test_image.png").

    Returns:
        np.array: The loaded image as a NumPy array with shape (height, width, channels).

    Requirements:
        - The image file must exist at the specified path.
        - The image must be in a format supported by the PIL library (e.g., PNG, JPEG).
        - The function should handle errors gracefully if the file is not found or the format is unsupported.

    Example:
        >>> image = load_image("./test_image.png")
        >>> print(image.shape)
        (480, 640, 3)
    """
    try:
        image = Image.open(image_path)
        image_array = np.array(image)
        return image_array
    except FileNotFoundError:
        print(f"Error: The file {image_path} does not exist.")
        return None
    except IOError:
        print(f"Error: Unable to read the file {image_path}.")
        return None