from synthesize_texture import synthesize_texture

def texture_synthesis_module(input_image_path: str, output_image_path: str, output_size: tuple[int, int]) -> None:
    """
    Synthesizes a texture using the Efros-Leung algorithm and saves the result as an image.

    This module-level function orchestrates the texture synthesis process by calling the `synthesize_texture` function.
    It ensures the input image is processed and the synthesized texture is saved to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./texture_icon.jpg").
    output_image_path : str
        The file path where the synthesized texture will be saved (e.g., "texture_synthesized.png").
    output_size : tuple[int, int]
        The desired size of the output image as a tuple of (width, height) in pixels (e.g., (128, 128)).

    Returns:
    --------
    None
        The function does not return any value. The synthesized texture is saved directly to the specified output path.
    """
    synthesize_texture(input_image_path, output_image_path, output_size)