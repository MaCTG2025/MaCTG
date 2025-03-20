from crop_middle_75_percent import crop_middle_75_percent

def image_cropping_module(input_image_path: str, output_image_path: str) -> None:
    """
    Module-level function for cropping the middle 75% of an input image and saving the result.

    This function uses the `crop_middle_75_percent` function to crop the middle 75% of the input image
    and save the cropped image to the specified output path.

    Args:
        input_image_path (str): The file path of the input image to be cropped.
        output_image_path (str): The file path where the cropped image will be saved.

    Returns:
        None: The function does not return any value. It saves the cropped image directly to the
            specified output path.

    Example:
        image_cropping_module("./test_image.png", "./cropped_image.png")
    """
    crop_middle_75_percent(input_image_path, output_image_path)