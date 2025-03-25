from Image_Processing import process_image_with_mask_and_blur

def test_Image_Processing() -> None:
    """
    Test the Image Processing module to ensure that the functions are working as expected.
    """
    # Define test parameters
    image_path = "./test_image.png"  # Replace with the path to a valid test image
    output_path = "./final_image.png"
    radius = 100
    kernel_size = 15
    sigmaX = 10

    # Test the module
    try:
        process_image_with_mask_and_blur(image_path, output_path, radius, kernel_size, sigmaX)
        print("Test passed: Image processed and saved successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_Image_Processing()