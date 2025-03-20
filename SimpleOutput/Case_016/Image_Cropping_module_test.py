from Image_Cropping import image_cropping_module

def test_Image_Cropping(input_image_path: str, output_image_path: str) -> None:
    """
    Test the functionality of the Image_Cropping module.

    This function tests whether the module correctly crops the middle 75% of the input image
    and saves the result to the specified output path.

    Args:
        input_image_path (str): The file path of the input image to be cropped.
        output_image_path (str): The file path where the cropped image will be saved.

    Returns:
        None: The function does not return any value. It prints a success message if the test passes.
    """
    try:
        # Call the module function
        image_cropping_module(input_image_path, output_image_path)
        print("Test passed: The image was successfully cropped and saved.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Cropping("./test_image.png", "./cropped_image.png")