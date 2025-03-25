from template_matching_with_noise import template_matching_with_noise

def template_matching_with_noise_module(
    input_image_path: str,
    template_image_path: str,
    output_image_path: str,
    sigma: float = 1.0,
    mean: float = 0.0,
    rectangle_thickness: int = 2
) -> None:
    """
    Module-level function for performing template matching with Gaussian noise addition.
    This function adds Gaussian noise to the input image, performs template matching to locate the template,
    draws a red rectangle around the detected location, and saves the result.

    Args:
        input_image_path (str): Path to the input image file (e.g., "./wheres_waldo.jpg").
        template_image_path (str): Path to the template image file (e.g., "./waldo.jpg").
        output_image_path (str): Path to save the output image with the detected location (e.g., "wheres_waldo_detected.png").
        sigma (float, optional): Standard deviation of the Gaussian noise. Defaults to 1.0.
        mean (float, optional): Mean of the Gaussian noise. Defaults to 0.0.
        rectangle_thickness (int, optional): Thickness of the red rectangle to draw around the detected location. Defaults to 2.

    Returns:
        None: The function saves the output image to the specified path.
    """
    template_matching_with_noise(input_image_path, template_image_path, output_image_path, sigma, mean, rectangle_thickness)