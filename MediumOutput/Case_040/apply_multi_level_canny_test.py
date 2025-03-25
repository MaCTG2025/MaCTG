import unittest
from apply_multi_level_canny import apply_multi_level_canny
import numpy as np
import cv2

class TestApplyMultiLevelCanny(unittest.TestCase):
    def setUp(self):
        self.image = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(self.image, (25, 25), (75, 75), 255, -1)

    def test_apply_multi_level_canny(self):
        low_threshold = 50
        medium_threshold = 100
        high_threshold = 150

        result = apply_multi_level_canny(self.image, low_threshold, medium_threshold, high_threshold)

        # Check if the result is a valid NumPy array
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, self.image.shape)

        # Check if the result contains edges (non-zero values)
        self.assertTrue(np.any(result))

if __name__ == '__main__':
    unittest.main()