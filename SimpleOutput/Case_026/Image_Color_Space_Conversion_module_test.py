from Image_Color_Space_Conversion import image_color_space_conversion

def test_image_color_space_conversion(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the image_color_space_conversion function by converting an input image to the YUV color space
    and saving the resulting image.

    Args:
        input_image_path (str): The file path of the input image to be converted.
        output_image_path (str): The file path where the converted YUV image will be saved.

    Returns:
        None: The function does not return any value. It tests the functionality of the module.
    """
    # Call the function to test
    image_color_space_conversion(input_image_path, output_image_path)
    print(f"Image converted and saved to {output_image_path}")

if __name__ == '__main__':
    test_image_color_space_conversion("./test_image.png", "./yuv_image.png")