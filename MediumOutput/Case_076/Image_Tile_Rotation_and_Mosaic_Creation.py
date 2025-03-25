from divide_image_into_tiles import divide_image_into_tiles
from rotate_tiles import rotate_tiles
from reassemble_tiles_into_mosaic import reassemble_tiles_into_mosaic
from save_mosaic_image import save_mosaic_image
import numpy as np

def create_rotated_tiles_mosaic(image_path: str, output_path: str) -> None:
    """
    Given an image, divide it into 2x2 tiles, rotate each tile (0°, 90°, 180°, 270°),
    reassemble the tiles into a mosaic, and save the final image.

    Args:
        image_path (str): The file path of the input image.
        output_path (str): The file path where the final mosaic image will be saved.

    Returns:
        None
    """
    # Load the image
    image = np.array(Image.open(image_path))

    # Divide the image into tiles
    tiles = divide_image_into_tiles(image)

    # Rotate the tiles
    rotated_tiles = rotate_tiles(tiles)

    # Reassemble the tiles into a mosaic
    mosaic_image = reassemble_tiles_into_mosaic(rotated_tiles)

    # Save the mosaic image
    save_mosaic_image(mosaic_image, output_path)