import unittest
from detect_and_draw_corners import detect_and_draw_corners
import numpy as np
import cv2

class TestDetectAndDrawCorners(unittest.TestCase):
    def setUp(self):
        # Create a sample image with known corners
        self.image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.circle(self.image, (50, 50), 10, (255, 255, 255), -1)
        cv2.circle(self.image, (150, 150), 10, (255, 255, 255), -1)

    def test_default_parameters(self):
        result = detect_and_draw_corners(self.image)
        # Check if corners are detected and drawn
        self.assertTrue(np.any(result[:, :, 2] == 255))

    def test_custom_parameters(self):
        result = detect_and_draw_corners(self.image, max_corners=1, quality_level=0.9, min_distance=50, color=(0, 255, 0), radius=5, thickness=2)
        # Check if corners are detected and drawn with custom parameters
        self.assertTrue(np.any(result[:, :, 1] == 255))
        self.assertFalse(np.any(result[:, :, 2] == 255))

if __name__ == '__main__':
    unittest.main()