from apply_kernel_filter import apply_kernel_filter

def image_filtering_module(input_image_path: str) -> None:
    """
    Applies a 3x3 kernel filter to the input image and saves the result as "filtered_image.png".

    This module-level function uses the `apply_kernel_filter` function to process the input image.
    The kernel filter is a 3x3 matrix with all elements equal to 1/9, which is a simple averaging filter.
    The filtered image is saved as "filtered_image.png" in the current working directory.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png"). The image should be in a format
        supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. The filtered image is saved as "filtered_image.png".
    """
    apply_kernel_filter(input_image_path)