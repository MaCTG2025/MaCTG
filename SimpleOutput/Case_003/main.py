from typing import Tuple
from Image_Pyramid_Scaling import image_pyramid_scaling_module

def main(input_image_path: str) -> Tuple[str, str]:
    """
    Entry point for the image pyramid scaling project. This function processes an input image by performing
    upscaling and downscaling using the `image_pyramid_scaling_module` function.

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
    return image_pyramid_scaling_module(input_image_path)

if __name__ == '__main__':
    main("./test_image.png")