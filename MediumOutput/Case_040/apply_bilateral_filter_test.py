import unittest
from apply_bilateral_filter import apply_bilateral_filter
import cv2
import numpy as np

class TestApplyBilateralFilter(unittest.TestCase):
    def test_apply_bilateral_filter(self):
        # Test with valid parameters
        result = apply_bilateral_filter('path_to_test_image.jpg', 9, 75, 75)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, np.ndarray)

        # Test with invalid image path
        with self.assertRaises(ValueError):
            apply_bilateral_filter('non_existent_image.jpg', 9, 75, 75)

        # Test with different values for d, sigmaColor, and sigmaSpace
        result1 = apply_bilateral_filter('path_to_test_image.jpg', 5, 50, 50)
        result2 = apply_bilateral_filter('path_to_test_image.jpg', 15, 100, 100)
        self.assertNotEqual(np.array_equal(result1, result2), True)

if __name__ == '__main__':
    unittest.main()