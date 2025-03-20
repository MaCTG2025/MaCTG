from typing import Tuple
from perform_pyramid_scaling import perform_pyramid_scaling

def image_pyramid_scaling_module(input_image_path: str) -> Tuple[str, str]:
    """
    Perform pyramid scaling (upscaling and downscaling) on an input image and save the results.

    This module-level function uses the `perform_pyramid_scaling` function to process an input image.
    It performs two pyramid scalings: upscaling and downscaling, and saves the resulting images.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image that needs to be processed. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    Tuple[str, str]
        A tuple containing two strings:
        1. The file path to the upscaled image ("upscaled.png").
        2. The file path to the downscaled image ("downscaled.png").
    """
    return perform_pyramid_scaling(input_image_path)