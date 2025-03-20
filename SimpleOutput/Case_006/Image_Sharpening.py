from load_image import load_image
from apply_sharpening_filter import apply_sharpening_filter

def sharpen_image(input_image_path: str, output_image_path: str) -> None:
    """
    Sharpens the input image using a predefined sharpening filter and saves the result.

    Args:
        input_image_path (str): The file path of the input image to be processed.
        output_image_path (str): The file path where the sharpened image will be saved.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input image file does not exist.
        ValueError: If the input image is not a valid format or the output path is invalid.
    """
    image = load_image(input_image_path)
    apply_sharpening_filter(input_image_path, output_image_path)