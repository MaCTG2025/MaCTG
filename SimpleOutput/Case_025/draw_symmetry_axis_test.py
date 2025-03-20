import unittest
from draw_symmetry_axis import draw_symmetry_axis
import numpy as np
import cv2

class TestDrawSymmetryAxis(unittest.TestCase):
    def test_no_symmetry_axis(self):
        # Create a sample image
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Call the function without providing an axis_x value
        result_image = draw_symmetry_axis(image, None)
        
        # Check that the image remains unchanged
        self.assertTrue(np.array_equal(result_image, image))

    def test_with_symmetry_axis(self):
        # Create a sample image
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Define the symmetry axis
        axis_x = 50
        
        # Call the function with the symmetry axis
        result_image = draw_symmetry_axis(image, axis_x)
        
        # Check that a green line has been drawn at the specified axis_x
        expected_line = np.full((100, 2, 3), [0, 255, 0], dtype=np.uint8)
        expected_result = np.copy(image)
        expected_result[:, axis_x-1:axis_x+1] = expected_line
        self.assertTrue(np.array_equal(result_image, expected_result))

if __name__ == '__main__':
    unittest.main()