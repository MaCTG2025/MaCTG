import unittest
from apply_gaussian_blur import apply_gaussian_blur
import numpy as np
import cv2

class TestApplyGaussianBlur(unittest.TestCase):

    def test_valid_input(self):
        # Create sample inputs
        grayscale_image = np.array([[100, 150, 200],
                                    [50, 100, 150],
                                    [200, 150, 100]], dtype=np.uint8)
        binary_mask = np.array([[0, 1, 0],
                               [1, 0, 1],
                               [0, 1, 0]], dtype=np.uint8)
        kernel_size = (3, 3)

        # Call the function
        result = apply_gaussian_blur(grayscale_image, binary_mask, kernel_size)

        # Verify the result is not None and has the same shape
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, grayscale_image.shape)

    def test_invalid_kernel_size(self):
        # Create sample inputs
        grayscale_image = np.array([[100, 150, 200],
                                    [50, 100, 150],
                                    [200, 150, 100]], dtype=np.uint8)
        binary_mask = np.array([[0, 1, 0],
                               [1, 0, 1],
                               [0, 1, 0]], dtype=np.uint8)
        kernel_size = (4, 4)

        # Call the function and expect an exception
        with self.assertRaises(ValueError):
            apply_gaussian_blur(grayscale_image, binary_mask, kernel_size)

    def test_mismatched_dimensions(self):
        # Create sample inputs
        grayscale_image = np.array([[100, 150, 200],
                                    [50, 100, 150]], dtype=np.uint8)
        binary_mask = np.array([[0, 1],
                               [1, 0]], dtype=np.uint8)
        kernel_size = (3, 3)

        # Call the function and expect an exception
        with self.assertRaises(ValueError):
            apply_gaussian_blur(grayscale_image, binary_mask, kernel_size)

if __name__ == '__main__':
    unittest.main()