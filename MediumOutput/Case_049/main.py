from modify_image_hue import modify_image_hue

def process_image_hue_modification(image_path: str) -> None:
    """
    Processes an image by modifying its Hue channel and saving the result.

    This function reads an image from the specified path, modifies its Hue channel
    by adding 50 (with wrapping around if necessary), and saves the modified image
    to disk as "hue_modified_image.png".

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed. The image should be in a format
        supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. The modified image is saved to disk.
    """
    modify_image_hue(image_path)

if __name__ == '__main__':
    process_image_hue_modification('./test_image.png')