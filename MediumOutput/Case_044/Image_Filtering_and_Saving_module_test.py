from Image_Filtering_and_Saving import image_filtering_and_saving

def test_Image_Filtering_and_Saving(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the functionality of the image_filtering_and_saving function by applying filters 
    and saving the processed image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.

    output_image_path : str
        The file path where the processed image will be saved.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the 
        function executes without errors.
    """
    try:
        image_filtering_and_saving(input_image_path, output_image_path)
        print("Test passed: Image filtering and saving completed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Filtering_and_Saving("./test_image.png", "final_image.png")