from Pencil_Sketch_Effect import apply_artistic_effects

def test_Pencil_Sketch_Effect(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the Pencil_Sketch_Effect module by applying artistic effects to an input image
    and saving the result to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png").
    output_image_path : str
        The file path where the processed image will be saved (e.g., "./pencil_sketch_image.png").

    Returns:
    --------
    None
        The function does not return any value. It verifies the functionality of the module by processing the image.
    """
    apply_artistic_effects(input_image_path, output_image_path)
    print(f"Artistic effects applied successfully. Output saved to {output_image_path}")

if __name__ == '__main__':
    test_Pencil_Sketch_Effect("./test_image.png", "./pencil_sketch_image.png")