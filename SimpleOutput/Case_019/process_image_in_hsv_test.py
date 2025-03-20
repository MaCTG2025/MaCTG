import unittest
from process_image_in_hsv import process_image_in_hsv
import cv2
import os

class TestProcessImageInHsv(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.expected_files = [
            "test_image_HSV.png",
            "test_image_hue_channel.png",
            "test_image_saturation_channel.png",
            "test_image_value_channel.png"
        ]

    def test_process_image_in_hsv(self):
        process_image_in_hsv(self.test_image_path)
        
        for expected_file in self.expected_files:
            self.assertTrue(os.path.exists(expected_file), f"File {expected_file} does not exist.")

if __name__ == "__main__":
    unittest.main()