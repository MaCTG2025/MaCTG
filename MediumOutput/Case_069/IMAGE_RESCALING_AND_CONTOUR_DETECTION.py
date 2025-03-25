from rescale_and_detect_contours import rescale_and_detect_contours

def image_rescaling_and_contour_detection(
    image_path: str,
    output_path_linear: str,
    output_path_cubic: str,
    contour_color: tuple = (255, 0, 0),
    contour_thickness: int = 3
) -> None:
    """
    Module-level function for rescaling an image to 2x size using linear and cubic interpolation,
    detecting contours, and saving the results.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.
    output_path_linear : str
        The file path where the rescaled image using linear interpolation will be saved.
    output_path_cubic : str
        The file path where the rescaled image using cubic interpolation will be saved.
    contour_color : tuple, optional
        The color of the detected contours in RGB format. Default is (255, 0, 0) (red).
    contour_thickness : int, optional
        The thickness of the detected contours. Default is 3.

    Returns:
    --------
    None
        The function saves the rescaled images with detected contours to the specified output paths.
    """
    rescale_and_detect_contours(
        image_path,
        output_path_linear,
        output_path_cubic,
        contour_color,
        contour_thickness
    )