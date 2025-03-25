import numpy as np
from PIL import Image

def divide_image_into_tiles(image: np.array) -> list[np.array]:
    """
    Divide the input image into a 2x2 grid of equal-sized tiles.

    Args:
        image (np.array): The input image as a NumPy array (height x width x channels).

    Returns:
        list[np.array]: A list of 4 NumPy arrays, each representing a tile of the image.
                        The tiles are ordered left-to-right, top-to-bottom.

    Requirements:
        1. The input image must be divisible into 4 equal-sized tiles (i.e., height and width must be even).
        2. Each tile should retain the same number of channels as the input image.
        3. The function should handle grayscale (2D) and RGB (3D) images.
    """
    # Check if the image dimensions are even
    if image.shape[0] % 2 != 0 or image.shape[1] % 2 != 0:
        raise ValueError("Image dimensions must be even to divide into 4 equal-sized tiles.")

    # Calculate the size of each tile
    tile_height = image.shape[0] // 2
    tile_width = image.shape[1] // 2

    # Initialize an empty list to store the tiles
    tiles = []

    # Loop through the image to extract each tile
    for i in range(2):
        for j in range(2):
            tile = image[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width]
            tiles.append(tile)

    return tiles