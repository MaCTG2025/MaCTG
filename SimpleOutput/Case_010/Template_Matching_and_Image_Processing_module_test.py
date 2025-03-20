from Template_Matching_and_Image_Processing import template_matching_and_image_processing

def test_Template_Matching_and_Image_Processing(input_image_path: str, template_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the Template_Matching_and_Image_Processing module.

    Args:
        input_image_path (str): The file path to the input image where the template will be searched.
        template_image_path (str): The file path to the template image that will be searched for within the input image.
        output_image_path (str): The file path where the resulting image with the bounding box will be saved.

    Returns:
        None: The function does not return any value. It prints a success message if the test passes.
    """
    try:
        template_matching_and_image_processing(input_image_path, template_image_path, output_image_path)
        print("Test passed: The function executed successfully and saved the output image.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Template_Matching_and_Image_Processing("./wheres_waldo.jpg", "./waldo.jpg", "waldo_image.png")