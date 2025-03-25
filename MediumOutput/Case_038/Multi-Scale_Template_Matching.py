from multi_scale_template_matching import multi_scale_template_matching

def multi_scale_template_matching_module(image_path: str, template_path: str, scales: list[float], output_path: str) -> None:
    """
    Perform multi-scale template matching on the input image using the provided template.

    This module-level function uses the `multi_scale_template_matching` function to scale the template,
    find the best match, draw a bounding box around the match, and save the resulting image.

    Args:
        image_path (str): Path to the input image where the template will be searched.
        template_path (str): Path to the template image that will be matched against the input image.
        scales (list[float]): List of scaling factors to apply to the template (e.g., [0.5, 0.75, 1.25, 1.5]).
        output_path (str): Path where the resulting image with the bounding box will be saved.

    Returns:
        None: The function saves the resulting image to the specified output path.
    """
    multi_scale_template_matching(image_path, template_path, scales, output_path)