import unittest
from calculate_and_save_differences import calculate_and_save_differences
import numpy as np
import os

class TestCalculateAndSaveDifferences(unittest.TestCase):

    def test_valid_input(self):
        # Create sample images with different interpolation methods
        linear_image = np.array([[10, 20], [30, 40]], dtype=np.uint8)
        cubic_image = np.array([[15, 25], [35, 45]], dtype=np.uint8)
        area_image = np.array([[12, 22], [32, 42]], dtype=np.uint8)

        # Call the function with valid input
        calculate_and_save_differences({
            'Linear': linear_image,
            'Cubic': cubic_image,
            'Area': area_image
        })

        # Check if the output files exist
        self.assertTrue(os.path.exists('diff_linear_cubic.npy'))
        self.assertTrue(os.path.exists('diff_cubic_area.npy'))
        self.assertTrue(os.path.exists('diff_area_linear.npy'))

        # Load the saved files and check their contents
        diff_linear_cubic = np.load('diff_linear_cubic.npy')
        diff_cubic_area = np.load('diff_cubic_area.npy')
        diff_area_linear = np.load('diff_area_linear.npy')

        expected_diff_linear_cubic = np.array([[-5, -5], [-5, -5]])
        expected_diff_cubic_area = np.array([[3, 3], [3, 3]])
        expected_diff_area_linear = np.array([[2, 2], [2, 2]])

        np.testing.assert_array_equal(diff_linear_cubic, expected_diff_linear_cubic)
        np.testing.assert_array_equal(diff_cubic_area, expected_diff_cubic_area)
        np.testing.assert_array_equal(diff_area_linear, expected_diff_area_linear)

        # Clean up the created files
        os.remove('diff_linear_cubic.npy')
        os.remove('diff_cubic_area.npy')
        os.remove('diff_area_linear.npy')

    def test_missing_key(self):
        # Create sample images with missing interpolation method
        linear_image = np.array([[10, 20], [30, 40]], dtype=np.uint8)
        cubic_image = np.array([[15, 25], [35, 45]], dtype=np.uint8)

        # Call the function with missing key
        with self.assertRaises(ValueError):
            calculate_and_save_differences({
                'Linear': linear_image,
                'Cubic': cubic_image
            })

    def test_different_dimensions(self):
        # Create sample images with different dimensions
        linear_image = np.array([[10, 20], [30, 40]], dtype=np.uint8)
        cubic_image = np.array([[15, 25], [35, 45], [55, 65]], dtype=np.uint8)
        area_image = np.array([[12, 22], [32, 42]], dtype=np.uint8)

        # Call the function with different dimensions
        with self.assertRaises(ValueError):
            calculate_and_save_differences({
                'Linear': linear_image,
                'Cubic': cubic_image,
                'Area': area_image
            })

if __name__ == '__main__':
    unittest.main()