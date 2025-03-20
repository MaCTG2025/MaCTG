from denoise_image import denoise_image

def image_denoising_module(input_image_path: str, output_image_path: str, h: int = 11, hForColorComponents: int = 6, templateWindowSize: int = 7, searchWindowSize: int = 21) -> None:
    """
    Perform fast mean denoising on an input image and save the denoised image to the specified output path.

    This module-level function uses the `denoise_image` function to reduce noise in the input image.
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
    image_denoising_module("./test_image.png", "denoised_image.png", h=11, hForColorComponents=6, templateWindowSize=7, searchWindowSize=21)
    """
    denoise_image(input_image_path, output_image_path, h, hForColorComponents, templateWindowSize, searchWindowSize)

if __name__ == '__main__':
    image_denoising_module("./test_image.png", "denoised_image.png", h=11, hForColorComponents=6, templateWindowSize=7, searchWindowSize=21)