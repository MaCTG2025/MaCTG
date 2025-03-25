from PIL import Image
import numpy as np

def load_image(image_path: str) -> np.array:
    """
    Load the input image from the specified file path.

    Args:
        image_path (str): The file path to the image to be loaded.

    Returns:
        np.array: A NumPy array representing the loaded image.

    Raises:
        FileNotFoundError: If the file does not exist at the specified path.
        ValueError: If the image format is unsupported.

    Example:
        >>> image = load_image("./test_image.png")
    """
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    
    try:
        image_array = np.array(image)
    except Exception as e:
        raise ValueError(f"Unsupported image format: {e}")
    
    return image_array