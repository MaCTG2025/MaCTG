import cv2
import numpy as np

def load_images(background_path: str, object_path: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Load the background image and the object image from their respective file paths.

    Args:
        background_path (str): The file path to the background image.
        object_path (str): The file path to the object image.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple containing the background image and the object image as NumPy arrays.

    Raises:
        FileNotFoundError: If either the background_path or object_path does not exist.
        IOError: If there is an error reading the image files.
    """
    try:
        background_image = cv2.imread(background_path)
        if background_image is None:
            raise IOError(f"Error reading background image from {background_path}")
        
        object_image = cv2.imread(object_path)
        if object_image is None:
            raise IOError(f"Error reading object image from {object_path}")
        
        return background_image, object_image
    
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except Exception as e:
        raise IOError(f"An error occurred while loading images: {e}")