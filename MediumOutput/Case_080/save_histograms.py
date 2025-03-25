import numpy as np
import os

def save_histograms(original_hist: np.ndarray, equalized_hist: np.ndarray, output_dir: str = ".") -> None:
    """
    Saves the original and equalized histograms to .npy files.

    Args:
        original_hist (np.ndarray, dtype=int): Original histogram of the grayscale image.
        equalized_hist (np.ndarray, dtype=int): Equalized histogram of the grayscale image.
        output_dir (str, optional): Directory where the histogram files will be saved. Defaults to the current directory.

    Returns:
        None (saves files: `original_histogram.npy` and `equalized_histogram.npy`).
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the histograms to .npy files
    np.save(os.path.join(output_dir, 'original_histogram.npy'), original_hist)
    np.save(os.path.join(output_dir, 'equalized_histogram.npy'), equalized_hist)