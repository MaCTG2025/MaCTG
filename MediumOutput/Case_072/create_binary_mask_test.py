import unittest
from create_binary_mask import create_binary_mask
import numpy as np

class TestCreateBinaryMask(unittest.TestCase):
    def test_create_binary_mask(self):
        # Test case with a simple gradient magnitude array
        gradient_magnitude = np.array([[30, 60], [90, 40]])
        expected_output = np.array([[0, 1], [1, 0]])
        self.assertTrue(np.array_equal(create_binary_mask(gradient_magnitude), expected_output))

        # Test case with a different threshold
        gradient_magnitude = np.array([[30, 60], [90, 40]])
        expected_output = np.array([[0, 1], [1, 0]])
        self.assertTrue(np.array_equal(create_binary_mask(gradient_magnitude, threshold=40), expected_output))

        # Test case with all values below the threshold
        gradient_magnitude = np.array([[20, 30], [40, 50]])
        expected_output = np.zeros((2, 2), dtype=int)
        self.assertTrue(np.array_equal(create_binary_mask(gradient_magnitude), expected_output))

        # Test case with all values above the threshold
        gradient_magnitude = np.array([[60, 70], [80, 90]])
        expected_output = np.ones((2, 2), dtype=int)
        self.assertTrue(np.array_equal(create_binary_mask(gradient_magnitude), expected_output))

        # Test case with an empty array
        gradient_magnitude = np.array([])
        expected_output = np.array([])
        self.assertTrue(np.array_equal(create_binary_mask(gradient_magnitude), expected_output))

if __name__ == '__main__':
    unittest.main()