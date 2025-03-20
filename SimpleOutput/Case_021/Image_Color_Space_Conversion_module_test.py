from Image_Color_Space_Conversion import image_color_space_conversion

def test_Image_Color_Space_Conversion(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the Image_Color_Space_Conversion module by converting an input image to the LAB color space and saving the result.

    Args:
        input_image_path (str): The file path of the input image to be converted.
                               Example: "./test_image.png"
        output_image_path (str): The file path where the LAB-converted image will be saved.
                                 Example: "lab_image.png"

    Returns:
        None: The function does not return any value. It verifies the correctness of the module by checking if the output file is created.
    """
    # Call the module function to convert the image
    image_color_space_conversion(input_image_path, output_image_path)

    # Verify that the output file is created
    import os
    if os.path.exists(output_image_path):
        print(f"Test passed: Output file '{output_image_path}' created successfully.")
    else:
        print(f"Test failed: Output file '{output_image_path}' not found.")

if __name__ == '__main__':
    test_Image_Color_Space_Conversion("./test_image.png", "lab_image.png")