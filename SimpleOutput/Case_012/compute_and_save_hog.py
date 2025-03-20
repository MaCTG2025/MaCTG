import numpy as np
from skimage.feature import hog
from skimage import io
import os

def compute_and_save_hog(image_path: str, cell_size: tuple[int, int], block_size: tuple[int, int], nbins: int, output_path: str) -> None:
    """
    Compute the Histogram of Oriented Gradients (HOG) for the input image and save the result as a .npy file.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by `skimage.io.imread` (e.g., PNG, JPEG).
    cell_size : tuple[int, int]
        The size of the cells in pixels (height, width) used for computing the HOG. Each cell will be divided into smaller blocks.
    block_size : tuple[int, int]
        The size of the blocks in cells (height, width) used for normalizing the HOG. Each block contains multiple cells.
    nbins : int
        The number of orientation bins used in the HOG computation. This determines the number of gradient orientations.
    output_path : str
        The file path where the computed HOG features will be saved as a .npy file.

    Returns:
    --------
    None
        The function does not return any value. The computed HOG features are saved to the specified output_path.

    Requirements:
    -------------
    1. The input image must be a valid image file readable by `skimage.io.imread`.
    2. The cell_size and block_size must be tuples of positive integers.
    3. The nbins must be a positive integer.
    4. The output_path must be a valid file path where the .npy file can be saved.

    Example:
    --------
    compute_and_save_hog(
        image_path="./test_image.png",
        cell_size=(8, 8),
        block_size=(2, 2),
        nbins=9,
        output_path="hog.npy"
    )
    """
    # Load the image
    image = io.imread(image_path)

    # Ensure the image is grayscale
    if len(image.shape) == 3:
        image = io.imread(image_path, as_gray=True)

    # Compute the HOG features
    hog_features, hog_image = hog(image, orientations=nbins, pixels_per_cell=cell_size, cells_per_block=block_size, visualize=True)

    # Check if the output directory exists, if not create it
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the HOG features to a .npy file
    np.save(output_path, hog_features)