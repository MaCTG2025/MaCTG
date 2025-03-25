import numpy as np
from Image_Processing_and_Histogram_Generation import process_and_save_histograms

def test_Image_Processing_and_Histogram_Generation(image_path: str, output_dir: str = ".") -> None:
    """
    Tests the basic functionality of the Image Processing and Histogram Generation module.

    Args:
        image_path (str): Path to the input image file.
        output_dir (str, optional): Directory where the histogram files will be saved. Defaults to the current directory.

    Returns:
        None
    """
    # Call the main function to process the image and save histograms
    process_and_save_histograms(image_path, output_dir)

    # Verify that the output files exist
    original_hist_file = f"{output_dir}/original_histogram.npy"
    equalized_hist_file = f"{output_dir}/equalized_histogram.npy"

    assert np.load(original_hist_file).dtype == int, "Original histogram file is not of type int."
    assert np.load(equalized_hist_file).dtype == int, "Equalized histogram file is not of type int."

    print("Test passed: Histogram files were generated and are of the correct type.")

if __name__ == '__main__':
    test_Image_Processing_and_Histogram_Generation("./test_image.png")