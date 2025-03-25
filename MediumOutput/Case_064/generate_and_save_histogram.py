import numpy as np

def generate_and_save_histogram(image: np.array, output_path: str) -> None:
    """
    Generate a histogram for the input image and save it as a .npy file.

    Args:
        image (np.array): The input image as a NumPy array with shape (height, width, channels).
        output_path (str): The path where the histogram will be saved (e.g., "original_hist.npy").

    Returns:
        None: The function saves the histogram directly to the specified output path.

    Requirements:
        - The input image must be a valid NumPy array.
        - The histogram should be computed for each channel (R, G, B) separately.
        - The histogram should be saved as a NumPy array in .npy format.
        - The function should handle errors gracefully if the output path is invalid.

    Example:
        >>> generate_and_save_histogram(image, "original_hist.npy")
        # Saves the histogram to "original_hist.npy"
    """
    try:
        # Compute histograms for each channel (R, G, B)
        histograms = [np.histogram(image[:, :, i], bins=256, range=(0, 256))[0] for i in range(3)]
        np.save(output_path, histograms)
    except Exception as e:
        print(f"An error occurred: {e}")