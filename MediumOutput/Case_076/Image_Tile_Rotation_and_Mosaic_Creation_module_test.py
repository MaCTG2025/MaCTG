from Image_Tile_Rotation_and_Mosaic_Creation import create_rotated_tiles_mosaic
import numpy as np
from PIL import Image

def test_Image_Tile_Rotation_and_Mosaic_Creation(image_path: str, output_path: str) -> None:
    """
    Test the functionality of the Image Tile Rotation and Mosaic Creation module.

    Args:
        image_path (str): The file path of the input image.
        output_path (str): The file path where the final mosaic image will be saved.

    Returns:
        None
    """
    # Call the module function
    create_rotated_tiles_mosaic(image_path, output_path)

    # Verify the output file exists
    try:
        with Image.open(output_path) as img:
            print(f"Output image saved successfully at {output_path}.")
            print(f"Image size: {img.size}")
    except Exception as e:
        print(f"Error: Output image could not be loaded. {e}")

if __name__ == '__main__':
    # Test with a sample image
    test_Image_Tile_Rotation_and_Mosaic_Creation("./test_image.png", "rotated_tiles.png")