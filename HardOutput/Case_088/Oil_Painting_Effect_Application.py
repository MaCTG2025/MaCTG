from apply_oil_painting_effect import apply_oil_painting_effect

def apply_oil_painting_effect_module(input_image_path: str, output_image_path: str) -> None:
    """
    Applies an oil painting effect to the input image and saves the processed image to the specified output path.

    Parameters:
        input_image_path (str): The file path of the input image to which the oil painting effect will be applied.
        output_image_path (str): The file path where the processed image will be saved.

    Returns:
        None
    """
    apply_oil_painting_effect(input_image_path, output_image_path)