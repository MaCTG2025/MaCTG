from apply_circular_mask import apply_circular_mask

def image_masking_module(input_image_path: str, output_image_path: str, mask_radius: int) -> None:
    """
    Applies a circular mask to an input image and saves the result.

    This module-level function uses the `apply_circular_mask` function to process an image by applying a circular mask
    centered at the image's center with the specified radius. The resulting image is saved to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").
    output_image_path : str
        The file path where the masked image will be saved (e.g., "masked_image.png").
    mask_radius : int
        The radius of the circular mask in pixels (e.g., 100).

    Returns:
    --------
    None
        The function does not return any value. It saves the resulting image to the specified output path.

    Example:
    --------
    image_masking_module("./test_image.png", "masked_image.png", 100)
    """
    apply_circular_mask(input_image_path, output_image_path, mask_radius)