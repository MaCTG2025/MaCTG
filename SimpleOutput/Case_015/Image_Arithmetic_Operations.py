from apply_image_arithmetic_operations import apply_image_arithmetic_operations

def image_arithmetic_module(image_path: str, value: int) -> Tuple[str, str]:
    """
    Applies arithmetic addition and subtraction operations to an input image.

    This module-level function uses the `apply_image_arithmetic_operations` function to perform
    arithmetic operations on the input image and returns the paths to the resulting images.

    Args:
        image_path (str): The file path to the input image. The image should be in a format supported by PIL (e.g., PNG, JPEG).
        value (int): The integer value to use for the arithmetic addition and subtraction operations.

    Returns:
        Tuple[str, str]: A tuple containing the file paths to the saved images:
            - added_image_path (str): The file path to the image after applying the addition operation.
            - subtracted_image_path (str): The file path to the image after applying the subtraction operation.
    """
    return apply_image_arithmetic_operations(image_path, value)