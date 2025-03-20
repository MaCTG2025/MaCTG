import cv2
from typing import Tuple

def perform_pyramid_scaling(input_image_path: str) -> Tuple[str, str]:
    """
    Perform pyramid scaling (upscaling and downscaling) on an input image and save the results.

    This function takes the path to an input image, performs two pyramid scalings:
    1. Upscaling: Increases the resolution of the image by a factor of 2 using OpenCV's `pyrUp` function.
    2. Downscaling: Decreases the resolution of the image by a factor of 2 using OpenCV's `pyrDown` function.

    The resulting images are saved as "upscaled.png" and "downscaled.png" in the current working directory.

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

    Requirements:
    -------------
    - The input image must exist at the specified path.
    - The function uses OpenCV for image processing, so the input image must be in a format supported by OpenCV.
    - The output images will be saved in the current working directory with the names "upscaled.png" and "downscaled.png".

    Example:
    --------
    >>> perform_pyramid_scaling("./test_image.png")
    ("./upscaled.png", "./downscaled.png")
    """
    # Read the input image
    image = cv2.imread(input_image_path)

    # Check if image is loaded properly
    if image is None:
        raise ValueError("Input image not found or unable to load.")

    # Upscale the image
    upscaled_image = cv2.pyrUp(image)
    cv2.imwrite("upscaled.png", upscaled_image)

    # Downscale the image
    downscaled_image = cv2.pyrDown(image)
    cv2.imwrite("downscaled.png", downscaled_image)

    # Return the paths to the saved images with leading './'
    return ("./upscaled.png", "./downscaled.png")