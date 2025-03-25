import numpy as np
from PIL import Image

def rotate_tiles(tiles: list[np.array]) -> list[np.array]:
    """
    Apply rotations (0°, 90°, 180°, and 270°) to each tile in the list.

    Args:
        tiles (list[np.array]): A list of 4 NumPy arrays, each representing a tile of the image.

    Returns:
        list[np.array]: A list of 4 NumPy arrays, each representing a rotated tile.
                        The rotations applied are 0°, 90°, 180°, and 270° respectively.

    Requirements:
        1. The first tile should remain unrotated (0°).
        2. The second tile should be rotated 90° clockwise.
        3. The third tile should be rotated 180° clockwise.
        4. The fourth tile should be rotated 270° clockwise.
        5. The function should handle grayscale (2D) and RGB (3D) images.
    """
    rotated_tiles = []
    for i, tile in enumerate(tiles):
        if i == 0:
            rotated_tiles.append(tile)
        elif i == 1:
            rotated_tiles.append(np.rot90(tile, k=-1))
        elif i == 2:
            rotated_tiles.append(np.rot90(tile, k=-2))
        elif i == 3:
            rotated_tiles.append(np.rot90(tile, k=-3))
    return rotated_tiles