import unittest
from convert_to_grayscale import convert_to_grayscale
import numpy as np
import cv2

class TestConvertToGrayscale(unittest.TestCase):
    def test_valid_rgb_image(self):
        # Create a sample RGB image
        height, width = 100, 100
        rgb_image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
        
        # Call the function
        grayscale_image = convert_to_grayscale(rgb_image)
        
        # Check if the output is a valid grayscale image
        self.assertIsNotNone(grayscale_image)
        self.assertEqual(grayscale_image.shape, (height, width))
        self.assertTrue(np.issubdtype(grayscale_image.dtype, np.uint8))

    def test_invalid_channels_image(self):
        # Create a sample image with invalid number of channels
        height, width = 100, 100
        invalid_image = np.random.randint(0, 256, size=(height, width, 4), dtype=np.uint8)
        
        # Call the function
        grayscale_image = convert_to_grayscale(invalid_image)
        
        # Check if the function handles the error gracefully
        self.assertIsNone(grayscale_image)

if __name__ == '__main__':
    unittest.main()