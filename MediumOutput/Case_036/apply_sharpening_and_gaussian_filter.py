import cv2
import numpy as np

def apply_sharpening_and_gaussian_filter(
    image_path: str,
    sharpening_kernel: np.ndarray,
    gaussian_kernel_size: tuple[int, int],
    sigmaX: int,
    output_path: str
) -> None:
    """
    Applies a sharpening filter and a Gaussian blur to an image.

    The function performs the following steps:
    1. Reads the image from the specified `image_path`.
    2. Applies a sharpening filter using the provided `sharpening_kernel`.
    3. Applies a Gaussian blur using the specified `gaussian_kernel_size` and `sigmaX`.
    4. Saves the processed image to the specified `output_path`.

    Parameters:
    -----------
    image_path : str
        The file path to the input image (e.g., "./test_image.png").
    sharpening_kernel : np.ndarray
        A 3x3 numpy array representing the sharpening kernel.
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

    Dependencies:
    -------------
    - OpenCV (`cv2`) for image processing.
    - NumPy (`numpy`) for array operations.

    Example Usage:
    --------------
    sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    apply_sharpening_and_gaussian_filter(
        image_path="./test_image.png",
        sharpening_kernel=sharpening_kernel,
        gaussian_kernel_size=(5, 5),
        sigmaX=5,
        output_path="sharpened_gaussian_image.png"
    )
    """
    # Read the image
    image = cv2.imread(image_path)

    # Apply the sharpening filter
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    # Apply the Gaussian blur
    blurred_image = cv2.GaussianBlur(sharpened_image, gaussian_kernel_size, sigmaX)

    # Save the processed image
    cv2.imwrite(output_path, blurred_image)