import unittest
from convert_to_grayscale import convert_to_grayscale
import cv2
import numpy as np

class TestConvertToGrayscale(unittest.TestCase):
    def test_convert_to_grayscale(self):
        # Load a sample image
        sample_image_path = './test_image.png'  # Ensure this path points to a valid test image
        expected_shape = (100, 100)  # Example shape, adjust according to your sample image
        
        # Call the function with the sample image path
        grayscale_image = convert_to_grayscale(sample_image_path)
        
        # Check if the returned image is a NumPy array
        self.assertIsInstance(grayscale_image, np.ndarray)
        
        # Check if the shape of the grayscale image matches the expected shape
        self.assertEqual(grayscale_image.shape[:2], expected_shape)
        
        # Check if the grayscale image is not empty
        self.assertGreater(grayscale_image.size, 0)

if __name__ == '__main__':
    unittest.main()