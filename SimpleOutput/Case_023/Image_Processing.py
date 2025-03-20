from process_image import process_image

def image_processing_module(input_image_path: str, output_image_path: str, blockSize: int = 11, C: int = 2) -> None:
    """
    Processes an input image by converting it to grayscale, applying adaptive thresholding, and saving the binary image.

    This module-level function encapsulates the functionality of the `process_image` function, which performs the following steps:
    1. Reads the input image from the specified path.
    2. Converts the image to grayscale.
    3. Applies adaptive thresholding using the Gaussian method and the inverse binary threshold type.
    4. Saves the resulting binary image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.
    output_image_path : str
        The file path where the processed binary image will be saved.
    blockSize : int, optional (default=11)
        The size of a pixel neighborhood used to calculate a threshold value for the pixel.
        Must be an odd integer greater than 1.
    C : int, optional (default=2)
        A constant subtracted from the mean or weighted mean to fine-tune the thresholding.

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved to the specified output path.

    Example:
    --------
    image_processing_module("./test_image.png", "binary_image.png", blockSize=11, C=2)
    """
    process_image(input_image_path, output_image_path, blockSize, C)