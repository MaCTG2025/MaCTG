from process_image import process_image

def image_processing_pipeline(image_path: str, output_path: str = "test_image_edges.png") -> None:
    """
    Processes an image by applying bilateral filtering, computing gradient magnitudes using Sobel operators,
    applying non-maximum suppression, and saving the processed image.

    Parameters:
    -----------
    image_path : str
        Path to the input image file.
    output_path : str, optional
        Path to save the processed image (default="test_image_edges.png").

    Returns:
    --------
    None
        The function saves the processed image to the specified `output_path`.
    """
    process_image(image_path, output_path=output_path)