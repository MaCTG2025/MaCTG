from locate_and_draw_bounding_box import locate_and_draw_bounding_box

def template_matching_and_image_processing(input_image_path: str, template_image_path: str, output_image_path: str) -> None:
    """
    Performs template matching on the input image, draws a bounding box around the matched region,
    and saves the resulting image.

    Args:
        input_image_path (str): The file path to the input image where the template will be searched.
        template_image_path (str): The file path to the template image that will be searched for within the input image.
        output_image_path (str): The file path where the resulting image with the bounding box will be saved.

    Returns:
        None: The function does not return any value. It saves the resulting image to the specified output path.
    """
    locate_and_draw_bounding_box(input_image_path, template_image_path, output_image_path)