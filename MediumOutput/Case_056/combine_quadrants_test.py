import unittest
from combine_quadrants import combine_quadrants
import numpy as np

class TestCombineQuadrants(unittest.TestCase):
    def test_combine_quadrants(self):
        # Create sample quadrants
        quadrant_size = (100, 100)
        top_left = np.ones(quadrant_size, dtype=np.uint8) * 255
        top_right = np.ones(quadrant_size, dtype=np.uint8) * 128
        bottom_left = np.ones(quadrant_size, dtype=np.uint8) * 64
        bottom_right = np.ones(quadrant_size, dtype=np.uint8) * 0

        # Combine the quadrants
        combined_image = combine_quadrants({
            'top_left': top_left,
            'top_right': top_right,
            'bottom_left': bottom_left,
            'bottom_right': bottom_right
        })

        # Check if the combined image has the correct shape
        expected_shape = (200, 200)
        self.assertEqual(combined_image.shape, expected_shape)

        # Check if the values in the combined image are correct
        expected_top_left = np.ones(quadrant_size, dtype=np.uint8) * 255
        expected_top_right = np.ones(quadrant_size, dtype=np.uint8) * 128
        expected_bottom_left = np.ones(quadrant_size, dtype=np.uint8) * 64
        expected_bottom_right = np.ones(quadrant_size, dtype=np.uint8) * 0

        self.assertTrue(np.array_equal(combined_image[0:100, 0:100], expected_top_left))
        self.assertTrue(np.array_equal(combined_image[0:100, 100:200], expected_top_right))
        self.assertTrue(np.array_equal(combined_image[100:200, 0:100], expected_bottom_left))
        self.assertTrue(np.array_equal(combined_image[100:200, 100:200], expected_bottom_right))

if __name__ == '__main__':
    unittest.main()