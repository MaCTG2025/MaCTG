from match_and_draw_contours import match_and_draw_contours

def image_matching_and_contour_drawing(input_image_path: str, template_image_path: str, output_image_path: str) -> None:
    """
    Finds the closest match of the template image in the input image, draws the contours of the match in red,
    and saves the resulting image.

    Args:
        input_image_path (str): The file path to the input image where the template will be matched.
        template_image_path (str): The file path to the template image that will be searched for in the input image.
        output_image_path (str): The file path where the resulting image with the drawn contours will be saved.

    Returns:
        None: The function does not return any value. It saves the resulting image to the specified output path.

    Example:
        image_matching_and_contour_drawing("./shapestomatch.jpg", "./4star.jpg", "matched_image.png")
    """
    match_and_draw_contours(input_image_path, template_image_path, output_image_path)