import unittest
from divide_into_quadrants import divide_into_quadrants
import numpy as np

class TestDivideIntoQuadrants(unittest.TestCase):
    def test_divide_into_quadrants(self):
        # Create a sample grayscale image
        image = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ], dtype=np.uint8)

        # Expected result
        expected_result = {
            'top_left': np.array([[1, 2], [5, 6]], dtype=np.uint8),
            'top_right': np.array([[3, 4], [7, 8]], dtype=np.uint8),
            'bottom_left': np.array([[9, 10], [13, 14]], dtype=np.uint8),
            'bottom_right': np.array([[11, 12], [15, 16]], dtype=np.uint8)
        }

        # Call the function
        result = divide_into_quadrants(image)

        # Check if the result matches the expected result
        self.assertEqual(result['top_left'].tolist(), expected_result['top_left'].tolist())
        self.assertEqual(result['top_right'].tolist(), expected_result['top_right'].tolist())
        self.assertEqual(result['bottom_left'].tolist(), expected_result['bottom_left'].tolist())
        self.assertEqual(result['bottom_right'].tolist(), expected_result['bottom_right'].tolist())

if __name__ == '__main__':
    unittest.main()