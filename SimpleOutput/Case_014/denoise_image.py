import cv2

def denoise_image(input_image_path: str, output_image_path: str, h: int = 11, hForColorComponents: int = 6, templateWindowSize: int = 7, searchWindowSize: int = 21) -> None:
    """
    Perform fast mean denoising on an input image and save the denoised image to the specified output path.

    This function uses OpenCV's `fastNlMeansDenoisingColored` method to reduce noise in the input image.
    The denoising parameters can be adjusted to control the strength and quality of the denoising process.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be denoised. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).
    
    output_image_path : str
        The file path where the denoised image will be saved. The output format is determined by the file extension (e.g., '.png').

    h : int, optional (default=11)
        Parameter regulating filter strength for luminance component. A larger value removes more noise but may also remove image details.

    hForColorComponents : int, optional (default=6)
        Parameter regulating filter strength for color components. Typically, this is the same as `h` or slightly smaller.

    templateWindowSize : int, optional (default=7)
        Size in pixels of the template patch used for denoising. Must be an odd integer.

    searchWindowSize : int, optional (default=21)
        Size in pixels of the window used for searching similar patches. Must be an odd integer.

    Returns:
    --------
    None
        The function does not return any value. The denoised image is saved to the specified `output_image_path`.

    Example:
    --------
    denoise_image("./test_image.png", "denoised_image.png", h=11, hForColorComponents=6, templateWindowSize=7, searchWindowSize=21)

    Notes:
    ------
    - The function assumes the input image is in color (3 channels). If the image is grayscale, use `fastNlMeansDenoising` instead.
    - Ensure the input image path is valid and accessible. The function will raise an error if the file does not exist.
    - The output image path should include a valid file extension (e.g., '.png', '.jpg') to determine the output format.
    """
    # Load the image from the input path
    image = cv2.imread(input_image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError("Input image could not be read.")

    # Apply fastNlMeansDenoisingColored to the image
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, h, hForColorComponents, templateWindowSize, searchWindowSize)

    # Save the denoised image to the output path
    cv2.imwrite(output_image_path, denoised_image)