from process_image_and_detect_corners import process_image_and_detect_corners

def process_image_and_detect_square_corners(image_path: str, output_path: str = "squares_with_corners.png") -> None:
    """
    Processes the input image to detect corners of squares, draws red circles on the detected corners,
    and saves the modified image to the specified output path.

    Args:
        image_path (str): The file path to the input image (e.g., "./squares.jpg").
        output_path (str, optional): The file path where the modified image will be saved. 
                                     Defaults to "squares_with_corners.png".

    Returns:
        None: The function does not return any value. It saves the modified image to the specified output path.

    Example:
        process_image_and_detect_square_corners("./squares.jpg", "output_image.png")
        # This will process "squares.jpg", detect corners, draw red circles, and save the result as "output_image.png".
    """
    process_image_and_detect_corners(image_path, output_path)