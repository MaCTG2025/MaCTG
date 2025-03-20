import cv2

def process_image(input_image_path: str, output_image_path: str, blockSize: int = 11, C: int = 2) -> None:
    """
    Processes an input image by converting it to grayscale, applying adaptive thresholding, and saving the binary image.

    The function performs the following steps:
    1. Reads the input image from the specified path.
    2. Converts the image to grayscale using OpenCV's `cvtColor` function.
    3. Applies adaptive thresholding using the Gaussian method (`cv2.ADAPTIVE_THRESH_GAUSSIAN_C`)
       and the inverse binary threshold type (`cv2.THRESH_BINARY_INV`).
    4. Saves the resulting binary image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.
    output_image_path : str
        The file path where the processed binary image will be saved.
    blockSize : int, optional (default=11)
        The size of a pixel neighborhood used to calculate a threshold value for the pixel.
        Must be an odd integer greater than 1.
    C : int, optional (default=2)
        A constant subtracted from the mean or weighted mean to fine-tune the thresholding.

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved to the specified output path.

    Requirements:
    -------------
    - The input image must exist at the specified `input_image_path`.
    - The `blockSize` must be an odd integer greater than 1.
    - The output directory must exist, or the function will raise an error if the path is invalid.

    Example:
    --------
    process_image("./test_image.png", "binary_image.png", blockSize=11, C=2)
    """
    # Read the input image
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, blockSize, C)

    # Save the binary image
    cv2.imwrite(output_image_path, binary_image)