import unittest
from divide_image_into_tiles import divide_image_into_tiles
import numpy as np
from PIL import Image

class TestDivideImageIntoTiles(unittest.TestCase):

    def test_divide_grayscale_image(self):
        # Create a sample grayscale image
        image_data = np.array([
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ], dtype=np.uint8)
        
        # Call the function
        tiles = divide_image_into_tiles(image_data)
        
        # Expected result
        expected_tile_1 = np.array([
            [0, 1],
            [4, 5]
        ], dtype=np.uint8)
        
        expected_tile_2 = np.array([
            [2, 3],
            [6, 7]
        ], dtype=np.uint8)
        
        expected_tile_3 = np.array([
            [8, 9],
            [12, 13]
        ], dtype=np.uint8)
        
        expected_tile_4 = np.array([
            [10, 11],
            [14, 15]
        ], dtype=np.uint8)
        
        # Verify the results
        self.assertTrue(np.array_equal(tiles[0], expected_tile_1))
        self.assertTrue(np.array_equal(tiles[1], expected_tile_2))
        self.assertTrue(np.array_equal(tiles[2], expected_tile_3))
        self.assertTrue(np.array_equal(tiles[3], expected_tile_4))

    def test_divide_rgb_image(self):
        # Create a sample RGB image
        image_data = np.array([
            [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]],
            [[4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7]],
            [[8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11]],
            [[12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]
        ], dtype=np.uint8)
        
        # Call the function
        tiles = divide_image_into_tiles(image_data)
        
        # Expected result
        expected_tile_1 = np.array([
            [[0, 0, 0], [1, 1, 1]],
            [[4, 4, 4], [5, 5, 5]]
        ], dtype=np.uint8)
        
        expected_tile_2 = np.array([
            [[2, 2, 2], [3, 3, 3]],
            [[6, 6, 6], [7, 7, 7]]
        ], dtype=np.uint8)
        
        expected_tile_3 = np.array([
            [[8, 8, 8], [9, 9, 9]],
            [[12, 12, 12], [13, 13, 13]]
        ], dtype=np.uint8)
        
        expected_tile_4 = np.array([
            [[10, 10, 10], [11, 11, 11]],
            [[14, 14, 14], [15, 15, 15]]
        ], dtype=np.uint8)
        
        # Verify the results
        self.assertTrue(np.array_equal(tiles[0], expected_tile_1))
        self.assertTrue(np.array_equal(tiles[1], expected_tile_2))
        self.assertTrue(np.array_equal(tiles[2], expected_tile_3))
        self.assertTrue(np.array_equal(tiles[3], expected_tile_4))

    def test_odd_dimensions(self):
        # Create a sample image with odd dimensions
        image_data = np.array([
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ], dtype=np.uint8)
        
        # Expect a ValueError
        with self.assertRaises(ValueError):
            divide_image_into_tiles(image_data)

if __name__ == '__main__':
    unittest.main()