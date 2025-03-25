from process_image import process_image

def image_processing_module(input_image_path: str, output_image_path: str) -> None:
    """
    Processes an input image by converting it to grayscale, applying Gaussian Blur to the upper half,
    and saving the result to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. Example: "./test_image.png".
    output_image_path : str
        The file path where the processed image will be saved. Example: "test_image_filtered.png".

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved directly to the specified output path.

    Example Usage:
    --------------
    image_processing_module("./test_image.png", "test_image_filtered.png")
    """
    process_image(input_image_path, output_image_path)