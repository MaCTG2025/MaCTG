from load_image import load_image
from rescale_image import rescale_image
from calculate_and_save_differences import calculate_and_save_differences

def image_rescaling_and_pixel_intensity_comparison(image_path: str) -> None:
    """
    Given an image, rescale it using different interpolation methods (Linear, Cubic, Area),
    calculate pixel intensity differences between rescaled images, and save the results into .npy files.

    Args:
        image_path (str): The file path to the input image.

    Returns:
        None: The function saves the following .npy files:
            - "diff_linear_cubic.npy": Pixel intensity differences between Linear and Cubic rescaled images.
            - "diff_cubic_area.npy": Pixel intensity differences between Cubic and Area rescaled images.
            - "diff_area_linear.npy": Pixel intensity differences between Area and Linear rescaled images.

    Example:
        >>> image_rescaling_and_pixel_intensity_comparison("./test_image.png")
    """
    image = load_image(image_path)
    rescaled_images = {
        'Linear': rescale_image(image, 'BILINEAR', 0.5),
        'Cubic': rescale_image(image, 'BICUBIC', 0.5),
        'Area': rescale_image(image, 'BOX', 0.5)
    }
    calculate_and_save_differences(rescaled_images)

if __name__ == '__main__':
    image_rescaling_and_pixel_intensity_comparison("./test_image.png")