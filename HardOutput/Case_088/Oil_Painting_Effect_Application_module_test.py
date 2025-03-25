from Oil_Painting_Effect_Application import apply_oil_painting_effect_module

def test_Oil_Painting_Effect_Application(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the basic functionality of the Oil Painting Effect Application module.

    Parameters:
        input_image_path (str): The file path of the input image to test.
        output_image_path (str): The file path where the processed image will be saved.

    Returns:
        None
    """
    # Test the module by applying the oil painting effect
    apply_oil_painting_effect_module(input_image_path, output_image_path)
    print(f"Oil painting effect applied successfully. Output saved to {output_image_path}")

if __name__ == '__main__':
    test_Oil_Painting_Effect_Application("./test_image.png", "./output_image.png")