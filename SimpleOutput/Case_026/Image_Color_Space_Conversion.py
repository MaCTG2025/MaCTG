from convert_image_to_yuv import convert_image_to_yuv

def image_color_space_conversion(input_image_path: str, output_image_path: str) -> None:
    """
    Converts an input image to the YUV color space and saves the resulting image.

    Args:
        input_image_path (str): The file path of the input image to be converted.
        output_image_path (str): The file path where the converted YUV image will be saved.

    Returns:
        None: The function does not return any value. It saves the converted image directly
              to the specified output path.

    Example:
        image_color_space_conversion("./test_image.png", "./yuv_image.png")
    """
    convert_image_to_yuv(input_image_path, output_image_path)