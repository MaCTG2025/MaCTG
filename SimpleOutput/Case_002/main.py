from extract_and_save_rgb_channels import extract_and_save_rgb_channels

def process_image_channels(image_path: str) -> None:
    """
    Processes an RGB image by splitting it into its R, G, and B channels, creating three new RGB images where only one channel is non-zero,
    and saving them as 'red_channel.png', 'green_channel.png', and 'blue_channel.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input RGB image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves three images to disk:
        - 'red_channel.png': An RGB image where only the red channel is non-zero.
        - 'green_channel.png': An RGB image where only the green channel is non-zero.
        - 'blue_channel.png': An RGB image where only the blue channel is non-zero.
    """
    extract_and_save_rgb_channels(image_path)

if __name__ == '__main__':
    process_image_channels('./test_image.png')