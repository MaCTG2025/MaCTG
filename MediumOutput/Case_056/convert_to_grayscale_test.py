import unittest
from convert_to_grayscale import convert_to_grayscale
import cv2
import numpy as np

class TestConvertToGrayscale(unittest.TestCase):
    def test_convert_to_grayscale(self):
        # Load a sample image
        sample_image_path = 'path/to/sample/image.jpg'
        expected_shape = (1080, 1920)  # Example shape, adjust according to your sample image
        
        # Call the function
        grayscale_image = convert_to_grayscale(sample_image_path)
        
        # Check if the returned image is a NumPy array
        self.assertIsInstance(grayscale_image, np.ndarray)
        
        # Check if the shape of the grayscale image matches the expected shape
        self.assertEqual(grayscale_image.shape[:2], expected_shape)
        
        # Check if the image has been converted to grayscale (single channel)
        self.assertEqual(grayscale_image.ndim, 2)

if __name__ == '__main__':
    unittest.main()