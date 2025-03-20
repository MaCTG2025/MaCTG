import unittest
from extract_and_save_rgb_channels import extract_and_save_rgb_channels
import cv2
import numpy as np
import os

class TestExtractAndSaveRGBChannels(unittest.TestCase):
    def setUp(self):
        self.test_image_path = 'test_image.png'
        self.expected_files = ['red_channel.png', 'green_channel.png', 'blue_channel.png']
        
        # Create a test image with known values
        self.image_data = np.array([
            [[255, 0, 0], [0, 255, 0]],
            [[0, 0, 255], [255, 255, 0]]
        ], dtype=np.uint8)
        cv2.imwrite(self.test_image_path, self.image_data)

    def tearDown(self):
        # Clean up the test image and expected files
        for file_name in self.expected_files + [self.test_image_path]:
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_extract_and_save_rgb_channels(self):
        # Call the function under test
        extract_and_save_rgb_channels(self.test_image_path)
        
        # Check if the expected files were created
        for file_name in self.expected_files:
            self.assertTrue(os.path.exists(file_name))

        # Load the saved images and check their content
        red_channel_img = cv2.imread('red_channel.png')
        green_channel_img = cv2.imread('green_channel.png')
        blue_channel_img = cv2.imread('blue_channel.png')

        expected_red_channel = np.array([
            [[255, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [255, 0, 0]]
        ], dtype=np.uint8)
        expected_green_channel = np.array([
            [[0, 0, 0], [255, 0, 0]],
            [[0, 0, 0], [0, 255, 0]]
        ], dtype=np.uint8)
        expected_blue_channel = np.array([
            [[0, 0, 0], [0, 0, 0]],
            [[255, 0, 0], [0, 0, 255]]
        ], dtype=np.uint8)

        self.assertTrue(np.array_equal(red_channel_img, expected_red_channel))
        self.assertTrue(np.array_equal(green_channel_img, expected_green_channel))
        self.assertTrue(np.array_equal(blue_channel_img, expected_blue_channel))

if __name__ == '__main__':
    unittest.main()