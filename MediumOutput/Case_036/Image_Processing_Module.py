from apply_sharpening_and_gaussian_filter import apply_sharpening_and_gaussian_filter

def image_processing_module(
    image_path: str,
    sharpening_kernel: list[list[int]],
    gaussian_kernel_size: tuple[int, int],
    sigmaX: int,
    output_path: str
) -> None:
    """
    Processes an image by applying a sharpening filter and a Gaussian blur.

    This module-level function performs the following steps:
    1. Applies a sharpening filter to the image using the provided kernel.
    2. Applies a Gaussian blur to the sharpened image using the specified kernel size and sigmaX.
    3. Saves the processed image to the specified output path.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./test_image.png").
    sharpening_kernel : list[list[int]]
        A 3x3 nested list representing the sharpening kernel.
        Example: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]].
    gaussian_kernel_size : tuple[int, int]
        The size of the Gaussian kernel as a tuple (width, height).
        Example: (5, 5).
    sigmaX : int
        The standard deviation of the Gaussian kernel in the X direction.
    output_path : str
        The file path where the processed image will be saved (e.g., "sharpened_gaussian_image.png").

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved to `output_path`.
    """
    apply_sharpening_and_gaussian_filter(
        image_path=image_path,
        sharpening_kernel=np.array(sharpening_kernel),
        gaussian_kernel_size=gaussian_kernel_size,
        sigmaX=sigmaX,
        output_path=output_path
    )