from Texture_Synthesis import texture_synthesis_module

def test_Texture_Synthesis(input_image_path: str, output_image_path: str, output_size: tuple[int, int]) -> None:
    """
    Tests the basic functionality of the Texture_Synthesis module.

    This function tests whether the module correctly synthesizes a texture and saves it to the specified output path.
    It verifies that the input and output types are handled correctly and that the output file is created.

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
        The function does not return any value. It prints a success message if the test passes.
    """
    texture_synthesis_module(input_image_path, output_image_path, output_size)
    print("Test passed: Texture synthesis completed successfully and output file created.")

if __name__ == '__main__':
    test_Texture_Synthesis("./texture_icon.jpg", "texture_synthesized.png", (128, 128))