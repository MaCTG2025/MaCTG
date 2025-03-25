from Image_Scaling_and_Histogram_Export import process_image_and_export_histograms

def test_Image_Scaling_and_Histogram_Export(image_path: str) -> None:
    """
    Test the functionality of the Image Scaling and Histogram Export module.

    Args:
        image_path (str): The path to the input image file (e.g., "./test_image.png").

    Returns:
        None: The function prints the results of the tests and saves histograms to files.
    """
    # Test the module by processing the image and exporting histograms
    process_image_and_export_histograms(image_path)
    print("Histograms saved successfully: original_hist.npy, upscaled_hist.npy, downscaled_hist.npy")

if __name__ == '__main__':
    test_Image_Scaling_and_Histogram_Export("./test_image.png")