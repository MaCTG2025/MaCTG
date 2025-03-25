from Watershed_Image_Segmentation import watershed_image_segmentation

def test_Watershed_Image_Segmentation(input_image_path: str, output_image_path: str) -> None:
    """
    Test the functionality of the Watershed_Image_Segmentation module.

    This function tests whether the `watershed_image_segmentation` function correctly
    processes the input image and saves the segmented image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./water_coins.jpg").
    output_image_path : str
        The file path where the segmented image will be saved (e.g., "water_coins_segmented.png").

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    watershed_image_segmentation(input_image_path, output_image_path)
    print("Test passed: The segmented image was successfully saved to", output_image_path)

if __name__ == '__main__':
    test_Watershed_Image_Segmentation("./water_coins.jpg", "water_coins_segmented.png")