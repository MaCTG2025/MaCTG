from compute_and_save_hog import compute_and_save_hog

def hog_computation_module(image_path: str, cell_size: tuple[int, int], block_size: tuple[int, int], nbins: int, output_path: str) -> None:
    """
    Module-level function to compute and save the Histogram of Oriented Gradients (HOG) for an input image.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by `skimage.io.imread` (e.g., PNG, JPEG).
    cell_size : tuple[int, int]
        The size of the cells in pixels (height, width) used for computing the HOG.
    block_size : tuple[int, int]
        The size of the blocks in cells (height, width) used for normalizing the HOG.
    nbins : int
        The number of orientation bins used in the HOG computation.
    output_path : str
        The file path where the computed HOG features will be saved as a .npy file.

    Returns:
    --------
    None
        The function does not return any value. The computed HOG features are saved to the specified output_path.
    """
    compute_and_save_hog(image_path, cell_size, block_size, nbins, output_path)

if __name__ == '__main__':
    hog_computation_module("./test_image.png", (8, 8), (2, 2), 9, "hog.npy")