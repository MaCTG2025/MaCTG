import unittest
from split_and_save_rgb_channels import split_and_save_rgb_channels
import os
import cv2

class TestSplitAndSaveRGBChannels(unittest.TestCase):
    def setUp(self):
        self.test_image_path = 'test_image.png'
        # Create a test image with known RGB values
        test_image = cv2.cvtColor(cv2.imread('path_to_test_image.png'), cv2.COLOR_BGR2RGB)
        cv2.imwrite(self.test_image_path, test_image)

    def tearDown(self):
        # Clean up the test image after tests
        os.remove(self.test_image_path)
        for filename in ['red_channel.png', 'green_channel.png', 'blue_channel.png']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_valid_image_path(self):
        split_and_save_rgb_channels(self.test_image_path)
        self.assertTrue(os.path.exists('red_channel.png'))
        self.assertTrue(os.path.exists('green_channel.png'))
        self.assertTrue(os.path.exists('blue_channel.png'))

    def test_invalid_image_path(self):
        with self.assertRaises(ValueError):
            split_and_save_rgb_channels('nonexistent_image.png')

    def test_non_rgb_image(self):
        non_rgb_image_path = 'non_rgb_image.jpg'  # Assuming this is a valid JPEG image
        with self.assertRaises(ValueError):
            split_and_save_rgb_channels(non_rgb_image_path)

if __name__ == '__main__':
    unittest.main()