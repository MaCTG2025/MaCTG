from extract_largest_connected_component import extract_largest_connected_component

def process_image_and_extract_largest_component(image_path: str) -> None:
    """
    Processes the input image to identify and extract the largest connected component (excluding the background),
    switches all other pixels to black, and saves the resulting image as 'largest_connected_component.png'.

    This module-level function uses the `extract_largest_connected_component` function to perform the task.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image as 'largest_connected_component.png'.
    """
    extract_largest_connected_component(image_path)