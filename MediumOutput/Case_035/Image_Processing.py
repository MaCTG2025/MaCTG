from process_image import process_image

def image_processing_module(image_path: str) -> None:
    """
    Applies a 3x3 Gaussian blur with sigmaX=5 and performs Canny edge detection on the input image.
    The resulting image is saved as 'canny_image.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image that needs to be processed. The image should be in a format
        supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved directly to the disk as 'canny_image.png'.

    Example:
    --------
    image_processing_module("./test_image.png")
    # This will apply Gaussian blur and Canny edge detection to 'test_image.png'
    # and save the result as 'canny_image.png'.
    """
    process_image(image_path)