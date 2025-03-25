import unittest
from compute_gradient_magnitude import compute_gradient_magnitude
import numpy as np
import cv2

class TestComputeGradientMagnitude(unittest.TestCase):

    def test_valid_image(self):
        # Create a sample image
        image = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]], dtype=np.uint8)

        # Compute the expected result manually
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        expected_result = np.sqrt(sobelx**2 + sobely**2)

        # Call the function
        result = compute_gradient_magnitude(image)

        # Check if the result matches the expected result
        self.assertTrue(np.allclose(result, expected_result))

    def test_invalid_input(self):
        # Invalid input (not a NumPy array)
        invalid_input = "This is not a NumPy array"

        # Check if the function raises a ValueError
        with self.assertRaises(ValueError):
            compute_gradient_magnitude(invalid_input)

if __name__ == '__main__':
    unittest.main()