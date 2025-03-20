from draw_ellipse_on_image import draw_ellipse_on_image

def process_image_with_ellipse(input_image_path: str, output_image_path: str) -> None:
    """
    Process an input image by drawing a green ellipse with fixed parameters and saving the result.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. The image should be in a format 
        supported by OpenCV (e.g., PNG, JPEG).
    output_image_path : str
        The file path where the resulting image with the ellipse drawn will be saved. 
        The output format will be determined by the file extension (e.g., '.png').

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved to the specified 
        output path.

    Example:
    --------
    process_image_with_ellipse("./test_image.png", "ellipse.png")
    """
    draw_ellipse_on_image(input_image_path, output_image_path)