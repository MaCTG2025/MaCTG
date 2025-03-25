from Image_Processing_and_Template_Matching import find_and_highlight_waldo

def test_Image_Processing_and_Template_Matching(image_path: str, template_path: str, output_path: str) -> None:
    """
    Tests the basic functionality of the Image Processing and Template Matching module.

    Args:
        image_path (str): Path to the input image file (e.g., "./wheres_waldo.jpg").
        template_path (str): Path to the template image file (e.g., "./waldo.jpg").
        output_path (str): Path to save the resulting image (e.g., "wheres_waldo_matched.png").

    Returns:
        None: The function tests the module and does not return anything.
    """
    # Call the main function of the module
    find_and_highlight_waldo(image_path, template_path, output_path)
    print(f"Test completed. Result saved to {output_path}")

if __name__ == '__main__':
    test_Image_Processing_and_Template_Matching("./wheres_waldo.jpg", "./waldo.jpg", "wheres_waldo_matched.png")