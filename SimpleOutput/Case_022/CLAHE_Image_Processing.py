from apply_clahe import apply_clahe

def clahe_image_processing(input_image_path: str, output_image_path: str, clipLimit: float = 2.0, tileGridSize: tuple = (8, 8)) -> None:
    """
    Processes an input image using Contrast Limited Adaptive Histogram Equalization (CLAHE) and saves the result.

    Args:
        input_image_path (str): The file path to the input image that needs to be processed.
        output_image_path (str): The file path where the processed image will be saved.
        clipLimit (float, optional): Threshold for contrast limiting. Defaults to 2.0.
        tileGridSize (tuple, optional): Size of the grid for histogram equalization. Defaults to (8, 8).

    Returns:
        None: The function does not return any value. The processed image is saved to the specified output path.

    Example:
        clahe_image_processing('./test_image.png', './clahe_image.png', clipLimit=2.0, tileGridSize=(8, 8))
    """
    apply_clahe(input_image_path, output_image_path, clipLimit, tileGridSize)