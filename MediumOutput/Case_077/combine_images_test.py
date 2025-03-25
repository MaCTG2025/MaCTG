import unittest
from combine_images import combine_images
import numpy as np

class TestCombineImages(unittest.TestCase):
    def test_combine_images(self):
        # Create sample input images and binary mask
        height, width = 5, 5
        blurred_image = np.array([[100, 100, 100, 100, 100],
                                  [100, 200, 200, 200, 100],
                                  [100, 200, 300, 200, 100],
                                  [100, 200, 200, 200, 100],
                                  [100, 100, 100, 100, 100]], dtype=np.uint8)
        grayscale_image = np.array([[50, 50, 50, 50, 50],
                                    [50, 150, 150, 150, 50],
                                    [50, 150, 250, 150, 50],
                                    [50, 150, 150, 150, 50],
                                    [50, 50, 50, 50, 50]], dtype=np.uint8)
        binary_mask = np.array([[0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0],
                               [0, 1, 1, 1, 0],
                               [0, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0]], dtype=np.uint8)

        # Expected output
        expected_output = np.array([[50, 50, 50, 50, 50],
                                   [50, 200, 200, 200, 50],
                                   [50, 200, 300, 200, 50],
                                   [50, 200, 200, 200, 50],
                                   [50, 50, 50, 50, 50]], dtype=np.uint8)

        # Call the function
        result = combine_images(blurred_image, grayscale_image, binary_mask)

        # Check if the result matches the expected output
        self.assertTrue(np.array_equal(result, expected_output))

    def test_mismatched_dimensions(self):
        # Create sample input images and binary mask with mismatched dimensions
        blurred_image = np.array([[100, 100, 100, 100, 100],
                                  [100, 200, 200, 200, 100],
                                  [100, 200, 300, 200, 100],
                                  [100, 200, 200, 200, 100],
                                  [100, 100, 100, 100, 100]], dtype=np.uint8)
        grayscale_image = np.array([[50, 50, 50, 50, 50],
                                    [50, 150, 150, 150, 50],
                                    [50, 150, 250, 150, 50],
                                    [50, 150, 150, 150, 50]], dtype=np.uint8)
        binary_mask = np.array([[0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0],
                               [0, 1, 1, 1, 0],
                               [0, 1, 1, 1, 0]], dtype=np.uint8)

        # Check if the function raises a ValueError when dimensions mismatch
        with self.assertRaises(ValueError):
            combine_images(blurred_image, grayscale_image, binary_mask)

if __name__ == '__main__':
    unittest.main()