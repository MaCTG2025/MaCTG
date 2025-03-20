from split_and_save_rgb_channels import split_and_save_rgb_channels

def process_image_channels(image_path: str) -> None:
    """
    Processes an RGB image by splitting it into its three color channels (Red, Green, Blue) and saving each channel as a separate grayscale PNG file.

    Args:
        image_path (str): The file path to the input RGB image. The image should be in PNG format.

    Returns:
        None: This function does not return any value. It saves the following files directly to disk:
            - "red_channel.png": Grayscale image representing the Red channel.
            - "green_channel.png": Grayscale image representing the Green channel.
            - "blue_channel.png": Grayscale image representing the Blue channel.

    Raises:
        ValueError: If the input image is not in RGB format or the file path is invalid.
    """
    split_and_save_rgb_channels(image_path)