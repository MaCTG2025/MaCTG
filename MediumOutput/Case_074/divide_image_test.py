import unittest
from divide_image import divide_image
import numpy as np

class TestDivideImage(unittest.TestCase):
    def test_divide_image(self):
        # Create a sample image with even dimensions
        sample_image = np.array([
            [[255, 0, 0], [0, 255, 0]],
            [[0, 0, 255], [255, 255, 0]]
        ], dtype=np.uint8)
        
        # Expected result after dividing the image
        expected_result = [
            np.array([[[255, 0, 0]]], dtype=np.uint8),
            np.array([[[0, 255, 0]]], dtype=np.uint8),
            np.array([[[0, 0, 255]]], dtype=np.uint8),
            np.array([[[255, 255, 0]]], dtype=np.uint8)
        ]
        
        # Call the function
        result = divide_image(sample_image)
        
        # Check if the result matches the expected output
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            np.testing.assert_array_equal(result[i], expected_result[i])

    def test_divide_image_odd_dimensions(self):
        # Create a sample image with odd dimensions
        sample_image = np.array([
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [255, 0, 255], [0, 255, 255]]
        ], dtype=np.uint8)
        
        # Test if the function raises a ValueError for odd dimensions
        with self.assertRaises(ValueError):
            divide_image(sample_image)

if __name__ == '__main__':
    unittest.main()