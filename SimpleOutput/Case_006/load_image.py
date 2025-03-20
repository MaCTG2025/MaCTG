from PIL import Image  # For image manipulation

def load_image(image_path: str) -> Image.Image:
    """
    Loads the input image from the specified path.

    Args:
        image_path (str): The file path of the input image to be loaded.

    Returns:
        Image.Image: The loaded image object.

    Raises:
        FileNotFoundError: If the image file does not exist at the specified path.
        ValueError: If the file is not a valid image format.
    """
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    except IOError:
        raise ValueError(f"The file is not a valid image format: {image_path}")