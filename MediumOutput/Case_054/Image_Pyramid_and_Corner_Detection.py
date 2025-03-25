from process_image_with_pyramid_and_corners import process_image_with_pyramid_and_corners

def image_pyramid_and_corner_detection(image_path: str, scales: List[float]) -> None:
    """
    Perform pyramid downscaling and Shi-Tomasi corner detection on the input image at specified scales,
    and save the resulting images with detected corners.

    Parameters:
    -----------
    image_path : str
        The path to the input image file (e.g., "./test_image.png").
    scales : List[float]
        A list of scaling factors for pyramid downscaling (e.g., [1.0, 0.5, 0.25]).

    Returns:
    --------
    None
        The function saves the resulting images to disk with filenames based on the scaling factors.
        For example, if the input image is "test_image.png", the output images will be saved as:
        - "test_image_corners_x1.png" (scale factor 1.0)
        - "test_image_corners_x0.5.png" (scale factor 0.5)
        - "test_image_corners_x0.25.png" (scale factor 0.25)
    """
    process_image_with_pyramid_and_corners(image_path, scales)