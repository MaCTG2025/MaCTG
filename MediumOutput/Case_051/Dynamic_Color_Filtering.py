from apply_dynamic_color_filter import apply_dynamic_color_filter

def dynamic_color_filter_module(image_path: str, brightness_threshold: int = 150) -> None:
    """
    Applies dynamic color filtering to an image based on pixel brightness. Converts regions
    with brightness above the specified threshold to grayscale and saves the result as
    'filtered_image.png'.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed. The image should be in a format
        supported by the PIL library (e.g., PNG, JPEG).

    brightness_threshold : int, optional (default=150)
        The brightness threshold value. Pixels with brightness above this value will be
        converted to grayscale.

    Returns:
    --------
    None
        The processed image is saved as 'filtered_image.png' in the current working directory.
    """
    apply_dynamic_color_filter(image_path, brightness_threshold)