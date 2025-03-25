import unittest
from apply_median_filter import apply_median_filter
import numpy as np

class TestApplyMedianFilter(unittest.TestCase):
    def test_apply_median_filter_grayscale(self):
        # Create a sample grayscale image
        image = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]], dtype=np.uint8)
        
        # Apply median filter with kernel size 3
        filtered_image = apply_median_filter(image, 3)
        
        # Expected result after applying median filter
        expected_result = np.array([[2, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 8]], dtype=np.uint8)
        
        self.assertTrue(np.array_equal(filtered_image, expected_result))

    def test_apply_median_filter_color(self):
        # Create a sample color image
        image = np.array([[[1, 2, 3], [4, 5, 6]],
                          [[7, 8, 9], [10, 11, 12]]], dtype=np.uint8)
        
        # Apply median filter with kernel size 3
        filtered_image = apply_median_filter(image, 3)
        
        # Expected result after applying median filter
        expected_result = np.array([[[2, 2, 3], [4, 5, 6]],
                                    [[7, 8, 8], [10, 11, 12]]], dtype=np.uint8)
        
        self.assertTrue(np.array_equal(filtered_image, expected_result))

    def test_apply_median_filter_invalid_kernel_size(self):
        # Create a sample grayscale image
        image = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]], dtype=np.uint8)
        
        # Try to apply median filter with invalid kernel size
        with self.assertRaises(ValueError):
            apply_median_filter(image, 2)

if __name__ == '__main__':
    unittest.main()