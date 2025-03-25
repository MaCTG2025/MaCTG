import unittest
from detect_and_draw_contours import detect_and_draw_contours
import numpy as np
import cv2

class TestDetectAndDrawContours(unittest.TestCase):

    def test_binary_image(self):
        binary_image = np.zeros((100, 100), dtype=np.uint8)
        binary_image[30:70, 30:70] = 255
        color = (0, 0, 255)
        thickness = 2
        result = detect_and_draw_contours(binary_image, color, thickness)
        self.assertEqual(result.shape, (100, 100, 3))
        self.assertTrue(np.any(result[:, :, 2] == 255))

    def test_non_binary_image(self):
        non_binary_image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
        color = (0, 0, 255)
        thickness = 2
        with self.assertRaises(cv2.error):
            detect_and_draw_contours(non_binary_image, color, thickness)

    def test_invalid_color(self):
        binary_image = np.zeros((100, 100), dtype=np.uint8)
        invalid_color = (0, 0, 256)
        thickness = 2
        with self.assertRaises(ValueError):
            detect_and_draw_contours(binary_image, invalid_color, thickness)

    def test_negative_thickness(self):
        binary_image = np.zeros((100, 100), dtype=np.uint8)
        color = (0, 0, 255)
        negative_thickness = -1
        with self.assertRaises(ValueError):
            detect_and_draw_contours(binary_image, color, negative_thickness)

if __name__ == '__main__':
    unittest.main()