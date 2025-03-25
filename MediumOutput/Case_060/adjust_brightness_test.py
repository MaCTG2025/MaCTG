import unittest
from adjust_brightness import adjust_brightness
import cv2
import numpy as np

class TestAdjustBrightness(unittest.TestCase):
    def test_adjust_brightness(self):
        # Load an example image
        image_path = "path_to_your_example_image.jpg"
        original_image = cv2.imread(image_path)
        
        # Adjust brightness using the function
        brightened_image = adjust_brightness(image_path)
        
        # Check if the image was loaded successfully
        self.assertIsNotNone(original_image)
        
        # Check if the brightened image has the correct shape
        self.assertEqual(brightened_image.shape, original_image.shape)
        
        # Check if the pixel values have been adjusted correctly
        for i in range(original_image.shape[0]):
            for j in range(original_image.shape[1]):
                for k in range(3):
                    original_pixel_value = original_image[i, j, k]
                    brightened_pixel_value = brightened_image[i, j, k]
                    self.assertTrue(brightened_pixel_value >= original_pixel_value)
                    self.assertTrue(brightened_pixel_value <= original_pixel_value + 50)

if __name__ == '__main__':
    unittest.main()