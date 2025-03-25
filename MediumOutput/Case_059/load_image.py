from PIL import Image
import numpy as np

def load_image(image_path: str) -> np.array:
    """
    Load the input image from the specified file path.

    Args:
        image_path (str): The file path of the input image.

    Returns:
        np.array: The image as a NumPy array with shape (height, width, channels).

    Raises:
        FileNotFoundError: If the image file does not exist at the specified path.
        ValueError: If the image file is corrupted or cannot be read.

    Requirements:
        - The image must be in a format supported by the PIL library (e.g., PNG, JPEG).
        - The function should handle file not found errors gracefully and provide meaningful error messages.
    """
    try:
        image = Image.open(image_path)
        image_array = np.array(image)
        return image_array
    except FileNotFoundError:
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")
    except Exception as e:
        raise ValueError(f"Error reading the image file '{image_path}': {e}")