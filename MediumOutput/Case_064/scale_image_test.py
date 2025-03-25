import unittest
from scale_image import scale_image
import numpy as np
from PIL import Image

class TestScaleImage(unittest.TestCase):
    def test_scale_up(self):
        # Create a sample image
        sample_image = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Define the scale factor
        scale_factor = 2.0
        
        # Call the function
        scaled_image = scale_image(sample_image, scale_factor)
        
        # Check if the dimensions are correct
        self.assertEqual(scaled_image.shape, (960, 1280, 3))
    
    def test_scale_down(self):
        # Create a sample image
        sample_image = np.zeros((960, 1280, 3), dtype=np.uint8)
        
        # Define the scale factor
        scale_factor = 0.5
        
        # Call the function
        scaled_image = scale_image(sample_image, scale_factor)
        
        # Check if the dimensions are correct
        self.assertEqual(scaled_image.shape, (480, 640, 3))
    
    def test_aspect_ratio_preservation(self):
        # Create a sample image
        sample_image = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Define the scale factor
        scale_factor = 1.5
        
        # Call the function
        scaled_image = scale_image(sample_image, scale_factor)
        
        # Check if the aspect ratio is preserved
        self.assertEqual(scaled_image.shape[0] / scaled_image.shape[1], sample_image.shape[0] / sample_image.shape[1])
    
    def test_invalid_scale_factor(self):
        # Create a sample image
        sample_image = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Define an invalid scale factor
        scale_factor = -1.0
        
        # Check if the function raises a ValueError
        with self.assertRaises(ValueError):
            scale_image(sample_image, scale_factor)

if __name__ == '__main__':
    unittest.main()