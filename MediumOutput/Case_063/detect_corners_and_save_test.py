import unittest
from detect_corners_and_save import detect_corners_and_save
import numpy as np
import os
import cv2

class TestDetectCornersAndSave(unittest.TestCase):
    def setUp(self):
        self.test_image = np.zeros((100, 100), dtype=np.uint8)
        cv2.circle(self.test_image, (50, 50), 10, 255, -1)
        self.output_path = "test_output.png"

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_valid_grayscale_image(self):
        detect_corners_and_save(self.test_image, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_non_grayscale_image(self):
        color_image = np.zeros((100, 100, 3), dtype=np.uint8)
        with self.assertRaises(ValueError):
            detect_corners_and_save(color_image, self.output_path)

    def test_invalid_output_path(self):
        invalid_path = "/path/that/does/not/exist/test_output.png"
        with self.assertRaises(FileNotFoundError):
            detect_corners_and_save(self.test_image, invalid_path)

if __name__ == "__main__":
    unittest.main()