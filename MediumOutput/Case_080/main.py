import numpy as np
from process_image import process_image
from save_histograms import save_histograms

def process_and_save_histograms(image_path: str, output_dir: str = ".") -> None:
    """
    Processes an image to convert it to grayscale, applies histogram equalization, and saves the original
    and equalized histograms to .npy files in the specified output directory.

    Args:
        image_path (str): Path to the input image file. The image must be in a format supported by OpenCV (e.g., PNG, JPEG).
        output_dir (str, optional): Directory where the histogram files will be saved. Defaults to the current directory.

    Returns:
        None (saves files: `original_histogram.npy` and `equalized_histogram.npy`).
    """
    # Process the image to get grayscale, equalized image, and histograms
    gray_image, equalized_image, original_hist, equalized_hist = process_image(image_path)

    # Save the histograms to .npy files
    save_histograms(original_hist, equalized_hist, output_dir)

if __name__ == '__main__':
    process_and_save_histograms("./test_image.png")