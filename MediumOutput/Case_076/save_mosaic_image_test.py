import unittest
from save_mosaic_image import save_mosaic_image
import numpy as np
from PIL import Image
import os

class TestSaveMosaicImage(unittest.TestCase):
    def test_save_grayscale_image(self):
        # Create a sample grayscale image
        mosaic_image = np.array([[0.1, 0.2], [0.3, 0.4]], dtype=np.float64)
        output_path = "test_grayscale.png"
        
        # Call the function
        save_mosaic_image(mosaic_image, output_path)
        
        # Check if the image is saved correctly
        with Image.open(output_path) as img:
            self.assertEqual(img.mode, 'L')
            self.assertEqual(img.size, (2, 2))
        
        # Clean up the test file
        os.remove(output_path)

    def test_save_rgb_image(self):
        # Create a sample RGB image
        mosaic_image = np.array([[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
                                [[0.7, 0.8, 0.9], [1.0, 1.1, 1.2]]], dtype=np.float64)
        output_path = "test_rgb.png"
        
        # Call the function
        save_mosaic_image(mosaic_image, output_path)
        
        # Check if the image is saved correctly
        with Image.open(output_path) as img:
            self.assertEqual(img.mode, 'RGB')
            self.assertEqual(img.size, (2, 2))
        
        # Clean up the test file
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()