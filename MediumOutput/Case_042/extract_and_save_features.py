import numpy as np
from skimage.feature import hog, local_binary_pattern
from skimage.io import imread
from skimage.color import rgb2gray

def extract_and_save_features(
    image_path: str,
    hog_cell_size: tuple[int, int] = (8, 8),
    hog_block_size: tuple[int, int] = (2, 2),
    hog_nbins: int = 9,
) -> None:
    """
    Extracts Histogram of Oriented Gradients (HOG) and Local Binary Pattern (LBP) features
    from the given image and saves them as .npy files.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        hog_cell_size (tuple[int, int]): Size of the cells for HOG feature extraction. 
            Default is (8, 8).
        hog_block_size (tuple[int, int]): Size of the blocks for HOG feature extraction. 
            Default is (2, 2).
        hog_nbins (int): Number of orientation bins for HOG feature extraction. 
            Default is 9.

    Returns:
        None: The function saves the extracted features directly to files:
            - HOG features are saved as "hog_features.npy".
            - LBP features are saved as "lbp_features.npy".

    Requirements:
        - The input image should be a valid image file (e.g., PNG, JPEG).
        - The image will be converted to grayscale before feature extraction.
        - The HOG features are computed using the specified cell size, block size, and number of bins.
        - The LBP features are computed using a radius of 1 and 8 neighboring points.
        - The function uses `skimage` for image processing and feature extraction.
        - The output files are saved in the current working directory.

    Example:
        extract_and_save_features("./test_image.png", hog_cell_size=(8, 8), hog_block_size=(2, 2), hog_nbins=9)
    """
    # Read the image
    image = imread(image_path)

    # Convert the image to grayscale
    gray_image = rgb2gray(image)

    # Compute HOG features
    hog_features = hog(gray_image, pixels_per_cell=hog_cell_size, cells_per_block=hog_block_size, orientations=hog_nbins, visualize=False)

    # Compute LBP features
    lbp_features = local_binary_pattern(gray_image, P=8, R=1, method="uniform")

    # Save the features to .npy files
    np.save("hog_features.npy", hog_features)
    np.save("lbp_features.npy", lbp_features)