import cv2

def apply_morphological_gradient(input_image_path: str) -> None:
    """
    Applies the morphological gradient operation to the input image using a 5x5 kernel with cv2.MORPH_RECT shape.
    The morphological gradient is calculated as the difference between the dilation and erosion of the image.
    The resulting image is saved as 'morphological_gradient.png' in the current working directory.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved as 'morphological_gradient.png'.

    Requirements:
    -------------
    - The input image must be a valid image file path.
    - The function uses OpenCV's `cv2.morphologyEx` with `cv2.MORPH_GRADIENT` to compute the morphological gradient.
    - A 5x5 rectangular kernel (`cv2.MORPH_RECT`) is used for the operation.
    - The resulting image is saved in the current working directory with the filename 'morphological_gradient.png'.

    Example:
    --------
    apply_morphological_gradient("./test_image.png")
    """
    # Load the input image
    image = cv2.imread(input_image_path)

    # Define the kernel size and shape
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Apply erosion
    eroded_image = cv2.erode(image, kernel)

    # Apply dilation
    dilated_image = cv2.dilate(image, kernel)

    # Calculate the morphological gradient
    morphological_gradient = cv2.subtract(dilated_image, eroded_image)

    # Save the result
    cv2.imwrite('morphological_gradient.png', morphological_gradient)