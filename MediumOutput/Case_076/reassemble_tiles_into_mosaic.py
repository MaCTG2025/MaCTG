from PIL import Image
import numpy as np

def reassemble_tiles_into_mosaic(rotated_tiles: list[np.array]) -> np.array:
    """
    Reassemble the rotated tiles into a mosaic-style image.

    Args:
        rotated_tiles (list[np.array]): A list of 4 NumPy arrays, each representing a rotated tile.

    Returns:
        np.array: A NumPy array representing the reassembled mosaic image.
    """
    # Assuming the tiles are already in the correct order and size
    # Create an empty image to hold the mosaic
    mosaic = Image.new('RGB', (rotated_tiles[0].shape[1] * 2, rotated_tiles[0].shape[0] * 2))
    
    # Paste each tile into the correct position in the mosaic
    mosaic.paste(Image.fromarray(rotated_tiles[0]), (0, 0))
    mosaic.paste(Image.fromarray(rotated_tiles[1]), (rotated_tiles[0].shape[1], 0))
    mosaic.paste(Image.fromarray(rotated_tiles[2]), (0, rotated_tiles[0].shape[0]))
    mosaic.paste(Image.fromarray(rotated_tiles[3]), (rotated_tiles[0].shape[1], rotated_tiles[0].shape[0]))
    
    # Convert the mosaic back to a NumPy array
    return np.array(mosaic)