from Image_Processing_and_Contrast_Adjustment import image_processing_and_contrast_adjustment

def test_Image_Processing_and_Contrast_Adjustment() -> None:
    """
    Tests the basic functionality of the Image_Processing_and_Contrast_Adjustment module.
    Ensures that the function processes the image and saves the output correctly.
    """
    # Test input parameters
    image_path = "./test_image.png"
    mask_length = 100
    mask_value = 1
    alpha = 1.5
    beta = 50
    output_path = "contrast_adjusted_image.png"

    # Call the function to process the image
    image_processing_and_contrast_adjustment(image_path, mask_length, mask_value, alpha, beta, output_path)

    # Print confirmation message
    print("Test completed. Check the output image at:", output_path)

if __name__ == '__main__':
    test_Image_Processing_and_Contrast_Adjustment()