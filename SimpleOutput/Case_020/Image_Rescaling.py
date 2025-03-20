from rescale_and_save_image import rescale_and_save_image

def image_rescaling_module(input_image_path: str) -> None:
    """
    Module-level function for rescaling an image to twice its original size using Linear, Cubic, and Area Interpolation,
    and saving the resulting images to disk.

    Args:
        input_image_path (str): The file path to the input image that needs to be rescaled.
                               Example: "./test_image.png"

    Returns:
        None: This function does not return any value. It saves the rescaled images to disk with the following filenames:
              - "linear_interpolation.png" (rescaled using Linear Interpolation)
              - "cubic_interpolation.png" (rescaled using Cubic Interpolation)
              - "area_interpolation.png" (rescaled using Area Interpolation)

    Example Usage:
        image_rescaling_module("./test_image.png")
    """
    rescale_and_save_image(input_image_path)