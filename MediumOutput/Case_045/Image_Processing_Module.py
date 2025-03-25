from process_image import process_image

def image_processing_module(image_path: str, circle_radius: int, addition_value: int, subtraction_value: int, output_path: str) -> None:
    """
    Module-level function for processing an image by applying arithmetic operations to specific regions.

    This function uses the `process_image` function to:
    1. Load the image from the specified `image_path`.
    2. Apply arithmetic addition to the central circle region and subtraction to the outer region.
    3. Save the processed image to the specified `output_path`.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.
    circle_radius : int
        The radius of the central circle region in pixels. Must be a positive integer.
    addition_value : int
        The value to add to the pixel values in the central circle region.
    subtraction_value : int
        The value to subtract from the pixel values in the outer region.
    output_path : str
        The file path where the processed image will be saved.

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image to `output_path`.
    """
    process_image(image_path, circle_radius, addition_value, subtraction_value, output_path)