import unittest
from reassemble_tiles_into_mosaic import reassemble_tiles_into_mosaic
import numpy as np
from PIL import Image

class TestReassembleTilesIntoMosaic(unittest.TestCase):
    def test_reassemble_tiles_into_mosaic(self):
        # Create sample tiles
        tile1 = np.array([[255, 0, 0], [0, 255, 0]], dtype=np.uint8)
        tile2 = np.array([[0, 0, 255], [255, 255, 0]], dtype=np.uint8)
        tile3 = np.array([[0, 255, 255], [255, 0, 255]], dtype=np.uint8)
        tile4 = np.array([[255, 255, 255], [0, 0, 0]], dtype=np.uint8)
        
        # Call the function with the sample tiles
        result = reassemble_tiles_into_mosaic([tile1, tile2, tile3, tile4])
        
        # Create the expected result manually
        expected_result = np.zeros((4, 4, 3), dtype=np.uint8)
        expected_result[:2, :2] = tile1
        expected_result[:2, 2:] = tile2
        expected_result[2:, :2] = tile3
        expected_result[2:, 2:] = tile4
        
        # Check if the result matches the expected result
        self.assertTrue(np.array_equal(result, expected_result))

if __name__ == '__main__':
    unittest.main()