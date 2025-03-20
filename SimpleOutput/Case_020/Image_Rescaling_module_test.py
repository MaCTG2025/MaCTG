from Image_Rescaling import image_rescaling_module

def test_Image_Rescaling(input_image_path: str) -> None:
    """
    Test the functionality of the Image_Rescaling module.

    Args:
        input_image_path (str): The file path to the input image that needs to be rescaled.
                               Example: "./test_image.png"

    Returns:
        None: This function does not return any value. It tests the module by calling it and verifying the output files.
    """
    # Call the module function
    image_rescaling_module(input_image_path)

    # Verify that the output files exist
    output_files = ["linear_interpolation.png", "cubic_interpolation.png", "area_interpolation.png"]
    for file in output_files:
        try:
            with open(file, "r"):
                print(f"Test passed: {file} exists.")
        except FileNotFoundError:
            print(f"Test failed: {file} does not exist.")

if __name__ == '__main__':
    test_Image_Rescaling("./test_image.png")