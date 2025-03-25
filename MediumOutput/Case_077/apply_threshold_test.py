import unittest
from apply_threshold import apply_threshold
import numpy as np

class TestApplyThreshold(unittest.TestCase):

    def test_valid_threshold(self):
        # Create a sample grayscale image
        grayscale_image = np.array([[50, 100, 150],
                                    [200, 250, 30],
                                    [75, 125, 175]], dtype=np.uint8)
        
        # Define a valid threshold value
        threshold_value = 128
        
        # Expected output
        expected_output = np.array([[0, 0, 1],
                                   [1, 1, 0],
                                   [0, 1, 1]], dtype=np.uint8)
        
        # Call the function
        result = apply_threshold(grayscale_image, threshold_value)
        
        # Assert that the result matches the expected output
        self.assertTrue(np.array_equal(result, expected_output))

    def test_invalid_threshold_low(self):
        # Create a sample grayscale image
        grayscale_image = np.array([[50, 100, 150],
                                    [200, 250, 30],
                                    [75, 125, 175]], dtype=np.uint8)
        
        # Define an invalid threshold value (too low)
        threshold_value = -1
        
        # Assert that the function raises a ValueError
        with self.assertRaises(ValueError):
            apply_threshold(grayscale_image, threshold_value)

    def test_invalid_threshold_high(self):
        # Create a sample grayscale image
        grayscale_image = np.array([[50, 100, 150],
                                    [200, 250, 30],
                                    [75, 125, 175]], dtype=np.uint8)
        
        # Define an invalid threshold value (too high)
        threshold_value = 256
        
        # Assert that the function raises a ValueError
        with self.assertRaises(ValueError):
            apply_threshold(grayscale_image, threshold_value)

if __name__ == '__main__':
    unittest.main()