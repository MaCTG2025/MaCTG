from apply_morphological_gradient import apply_morphological_gradient

def apply_morphological_gradient_module(input_image_path: str) -> None:
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
    """
    apply_morphological_gradient(input_image_path)