import cv2

def apply_bilateral_filter(input_image_path: str, output_image_path: str, d: int = 9, sigmaColor: float = 75.0, sigmaSpace: float = 75.0) -> None:
    """
    Applies a bilateral filter to an input image to smooth it while preserving edges.

    The function reads an image from the specified input path, applies a bilateral filter
    with the given parameters, and saves the filtered image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.
    output_image_path : str
        The file path where the filtered image will be saved.
    d : int, optional (default=9)
        Diameter of each pixel neighborhood used during filtering.
    sigmaColor : float, optional (default=75.0)
        Filter sigma in the color space. A larger value means that farther colors within
        the pixel neighborhood will be mixed together, resulting in larger areas of semi-equal color.
    sigmaSpace : float, optional (default=75.0)
        Filter sigma in the coordinate space. A larger value means that farther pixels
        will influence each other as long as their colors are close enough.

    Returns:
    --------
    None
        The function does not return any value. The filtered image is saved to the specified output path.

    Requirements:
    -------------
    - The input image must be a valid image file (e.g., PNG, JPEG).
    - The output directory must exist and be writable.
    - The OpenCV library (cv2) must be installed and available for use.

    Example:
    --------
    apply_bilateral_filter("./test_image.png", "./bilateral_filtered_image.png", d=9, sigmaColor=75, sigmaSpace=75)
    """
    # Read the input image
    image = cv2.imread(input_image_path)

    # Apply the bilateral filter
    filtered_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

    # Save the filtered image
    cv2.imwrite(output_image_path, filtered_image)