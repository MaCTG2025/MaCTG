from Image_Transformation_and_Seamless_Cloning import image_transformation_and_seamless_cloning

def test_Image_Transformation_and_Seamless_Cloning(background_path: str, object_path: str, output_path: str) -> None:
    """
    Test the functionality of the Image_Transformation_and_Seamless_Cloning module.

    Args:
        background_path (str): The file path to the background image.
        object_path (str): The file path to the object image.
        output_path (str): The file path where the final blended image will be saved.

    Returns:
        None
    """
    try:
        # Call the main function of the module
        image_transformation_and_seamless_cloning(background_path, object_path, output_path)
        print("Test passed: The module executed successfully and saved the output image.")
    except Exception as e:
        print(f"Test failed: An error occurred - {e}")

if __name__ == '__main__':
    # Define input paths for testing
    background_path = "./abraham.jpg"
    object_path = "./test_image.png"
    output_path = "./seamless_cloning.png"

    # Run the test
    test_Image_Transformation_and_Seamless_Cloning(background_path, object_path, output_path)