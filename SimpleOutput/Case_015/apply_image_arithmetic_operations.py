from PIL import Image
import os
from typing import Tuple

def apply_image_arithmetic_operations(image_path: str, value: int) -> Tuple[str, str]:
    """
    Applies arithmetic addition and subtraction operations to an input image.

    This function reads an image from the specified path, applies arithmetic addition and subtraction
    operations using the provided value, and saves the resulting images as "added_image.png" and
    "substracted_image.png" in the same directory as the input image.

    Args:
        image_path (str): The file path to the input image. The image should be in a format supported by PIL (e.g., PNG, JPEG).
        value (int): The integer value to use for the arithmetic addition and subtraction operations.

    Returns:
        Tuple[str, str]: A tuple containing the file paths to the saved images:
            - added_image_path (str): The file path to the image after applying the addition operation.
            - subtracted_image_path (str): The file path to the image after applying the subtraction operation.

    Requirements:
        - The input image must exist at the specified path.
        - The value must be a valid integer.
        - The function uses the Python Imaging Library (PIL) for image processing.
        - The resulting images are saved in the same directory as the input image with filenames "added_image.png" and "substracted_image.png".

    Example:
        added_image_path, subtracted_image_path = apply_image_arithmetic_operations("./test_image.png", 100)
        # This will create "added_image.png" and "substracted_image.png" in the current directory.
    """
    # Open the image
    img = Image.open(image_path)

    # Apply addition
    added_img = Image.eval(img, lambda x: min(255, x + value))

    # Apply subtraction
    subtracted_img = Image.eval(img, lambda x: max(0, x - value))

    # Define output paths
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    added_image_path = f"{base_name}_added_image.png"
    subtracted_image_path = f"{base_name}_subtracted_image.png"

    # Save the images
    added_img.save(added_image_path)
    subtracted_img.save(subtracted_image_path)

    return added_image_path, subtracted_image_path