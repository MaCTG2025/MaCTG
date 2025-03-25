import unittest
from process_quadrants import process_quadrants
import cv2
import numpy as np

class TestProcessQuadrants(unittest.TestCase):
    def setUp(self):
        # Create sample quadrants for testing
        self.quadrant_size = (100, 100)
        self.top_left = np.zeros(self.quadrant_size, dtype=np.uint8)
        self.top_right = np.zeros(self.quadrant_size, dtype=np.uint8)
        self.bottom_left = np.zeros(self.quadrant_size, dtype=np.uint8)
        self.bottom_right = np.zeros(self.quadrant_size, dtype=np.uint8)

        # Fill quadrants with some values for testing
        self.top_left[25:75, 25:75] = 255
        self.top_right[25:75, 25:75] = 255
        self.bottom_left[25:75, 25:75] = 255
        self.bottom_right[25:75, 25:75] = 255

        self.quadrants = {
            'top_left': self.top_left,
            'top_right': self.top_right,
            'bottom_left': self.bottom_left,
            'bottom_right': self.bottom_right
        }

    def test_process_quadrants(self):
        result = process_quadrants(self.quadrants)

        # Check if the output is a dictionary
        self.assertIsInstance(result, dict)

        # Check if all keys are present
        self.assertIn('top_left', result)
        self.assertIn('top_right', result)
        self.assertIn('bottom_left', result)
        self.assertIn('bottom_right', result)

        # Check if the shapes of the processed images match the original shapes
        self.assertEqual(result['top_left'].shape, self.quadrant_size)
        self.assertEqual(result['top_right'].shape, self.quadrant_size)
        self.assertEqual(result['bottom_left'].shape, self.quadrant_size)
        self.assertEqual(result['bottom_right'].shape, self.quadrant_size)

        # Check if the types of the processed images are correct
        self.assertIsInstance(result['top_left'], np.ndarray)
        self.assertIsInstance(result['top_right'], np.ndarray)
        self.assertIsInstance(result['bottom_left'], np.ndarray)
        self.assertIsInstance(result['bottom_right'], np.ndarray)

        # Additional checks can be added here based on expected behavior

if __name__ == '__main__':
    unittest.main()