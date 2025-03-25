import unittest
from rotate_image import rotate_image
import numpy as np
import cv2

class TestRotateImage(unittest.TestCase):

    def test_rotate_image_valid_input(self):
        # Create a sample image
        sample_image = np.array([[1, 2], [3, 4]], dtype=np.uint8)
        
        # Expected result after rotating 90 degrees clockwise
        expected_result = np.array([[3, 1], [4, 2]], dtype=np.uint8)
        
        # Call the function with the sample image
        rotated_image = rotate_image(sample_image)
        
        # Check if the rotated image matches the expected result
        self.assertTrue(np.array_equal(rotated_image, expected_result))

    def test_rotate_image_invalid_input(self):
        # Create an invalid input (not a NumPy array)
        invalid_input = "This is not a NumPy array"
        
        # Check if the function raises a ValueError when given an invalid input
        with self.assertRaises(ValueError):
            rotate_image(invalid_input)

if __name__ == '__main__':
    unittest.main()