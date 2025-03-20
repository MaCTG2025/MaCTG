from Image_Processing_in_HSV_Color_Space import process_image_module

def test_Image_Processing_in_HSV_Color_Space(input_image_path: str) -> None:
    """
    Tests the functionality of the Image_Processing_in_HSV_Color_Space module by processing an input image
    and verifying that the output files are created.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function to process the image
    process_image_module(input_image_path)

    # Verify that the output files are created
    output_files = ["HSV.png", "hue_channel.png", "saturation_channel.png", "value_channel.png"]
    for file in output_files:
        if not os.path.exists(file):
            print(f"Test failed: {file} was not created.")
            return
    print("Test passed: All output files were created successfully.")

if __name__ == '__main__':
    test_Image_Processing_in_HSV_Color_Space("./test_image.png")