import unittest
from rescale_image import rescale_image
from PIL import Image
import numpy as np

class TestRescaleImage(unittest.TestCase):
    def test_rescale_image_linear(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        sample_image[30:70, 30:70] = 255
        
        # Rescale the image using linear interpolation
        rescaled_image = rescale_image(sample_image, 'Linear', 0.5)
        
        # Check if the dimensions are correct
        self.assertEqual(rescaled_image.shape, (50, 50, 3))
        
        # Check if the values are correctly scaled
        self.assertTrue(np.allclose(rescaled_image, 127.5))

    def test_rescale_image_cubic(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        sample_image[30:70, 30:70] = 255
        
        # Rescale the image using cubic interpolation
        rescaled_image = rescale_image(sample_image, 'Cubic', 2.0)
        
        # Check if the dimensions are correct
        self.assertEqual(rescaled_image.shape, (200, 200, 3))
        
        # Check if the values are correctly scaled
        self.assertTrue(np.allclose(rescaled_image, 127.5))

    def test_rescale_image_area(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        sample_image[30:70, 30:70] = 255
        
        # Rescale the image using area interpolation
        rescaled_image = rescale_image(sample_image, 'Area', 0.5)
        
        # Check if the dimensions are correct
        self.assertEqual(rescaled_image.shape, (50, 50, 3))
        
        # Check if the values are correctly scaled
        self.assertTrue(np.allclose(rescaled_image, 127.5))

    def test_rescale_image_unsupported_method(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        sample_image[30:70, 30:70] = 255
        
        # Try to rescale the image with an unsupported method
        with self.assertRaises(ValueError):
            rescale_image(sample_image, 'Bilinear', 0.5)

    def test_rescale_image_negative_scale_factor(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        sample_image[30:70, 30:70] = 255
        
        # Try to rescale the image with a negative scale factor
        with self.assertRaises(ValueError):
            rescale_image(sample_image, 'Linear', -0.5)

if __name__ == '__main__':
    unittest.main()