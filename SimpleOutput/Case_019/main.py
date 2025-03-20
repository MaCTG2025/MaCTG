from Image_Processing_in_HSV_Color_Space import process_image_module

def main(input_image_path: str) -> None:
    """
    Processes an input image by converting it to the HSV color space, splitting it into its channels,
    and saving the HSV image and its channels as separate files.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves the following files to disk:
        - "HSV.png": The image converted to the HSV color space.
        - "hue_channel.png": The Hue channel of the HSV image.
        - "saturation_channel.png": The Saturation channel of the HSV image.
        - "value_channel.png": The Value channel of the HSV image.

    Example:
    --------
    main("./test_image.png")
    """
    process_image_module(input_image_path)

if __name__ == '__main__':
    main("./test_image.png")