import unittest
from apply_adaptive_thresholding import apply_adaptive_thresholding
import numpy as np
import cv2

class TestAdaptiveThresholding(unittest.TestCase):
    def test_valid_input(self):
        # Create a sample grayscale image
        gray_image = np.array([[50, 100, 150],
                               [200, 250, 30]],
                              dtype=np.uint8)

        # Expected output for the given parameters
        expected_output = np.array([[0, 0, 0],
                                    [255, 255, 255]],
                                   dtype=np.uint8)

        # Call the function with valid parameters
        result = apply_adaptive_thresholding(gray_image, blockSize=3, C=2)

        # Check if the result matches the expected output
        self.assertTrue(np.array_equal(result, expected_output))

    def test_invalid_block_size_even(self):
        # Create a sample grayscale image
        gray_image = np.array([[50, 100, 150],
                               [200, 250, 30]],
                              dtype=np.uint8)

        # Try calling the function with an even block size
        with self.assertRaises(ValueError):
            apply_adaptive_thresholding(gray_image, blockSize=4, C=2)

    def test_invalid_block_size_less_than_or_equal_to_1(self):
        # Create a sample grayscale image
        gray_image = np.array([[50, 100, 150],
                               [200, 250, 30]],
                              dtype=np.uint8)

        # Try calling the function with a block size less than or equal to 1
        with self.assertRaises(ValueError):
            apply_adaptive_thresholding(gray_image, blockSize=1, C=2)

    def test_non_grayscale_image(self):
        # Create a sample color image
        color_image = np.array([[[50, 100, 150]],
                                [[200, 250, 30]]],
                               dtype=np.uint8)

        # Try calling the function with a non-grayscale image
        with self.assertRaises(cv2.error):
            apply_adaptive_thresholding(color_image, blockSize=3, C=2)

if __name__ == '__main__':
    unittest.main()