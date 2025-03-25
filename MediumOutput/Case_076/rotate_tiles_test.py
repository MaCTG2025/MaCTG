import unittest
from rotate_tiles import rotate_tiles
import numpy as np

class TestRotateTiles(unittest.TestCase):

    def test_rotate_tiles(self):
        # Create sample tiles
        tile_0 = np.array([[0, 1], [2, 3]], dtype=np.uint8)
        tile_1 = np.array([[4, 5], [6, 7]], dtype=np.uint8)
        tile_2 = np.array([[8, 9], [10, 11]], dtype=np.uint8)
        tile_3 = np.array([[12, 13], [14, 15]], dtype=np.uint8)

        tiles = [tile_0, tile_1, tile_2, tile_3]

        # Expected results
        expected_tile_0 = tile_0  # 0° rotation (no change)
        expected_tile_1 = np.array([[6, 4], [7, 5]], dtype=np.uint8)  # 90° rotation
        expected_tile_2 = np.array([[11, 10], [9, 8]], dtype=np.uint8)  # 180° rotation
        expected_tile_3 = np.array([[13, 15], [12, 14]], dtype=np.uint8)  # 270° rotation

        expected_tiles = [expected_tile_0, expected_tile_1, expected_tile_2, expected_tile_3]

        # Call the function
        result_tiles = rotate_tiles(tiles)

        # Check if the results match the expected values
        for i in range(len(result_tiles)):
            self.assertTrue(np.array_equal(result_tiles[i], expected_tiles[i]))

if __name__ == '__main__':
    unittest.main()