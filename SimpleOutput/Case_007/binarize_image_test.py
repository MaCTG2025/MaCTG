import unittest
from binarize_image import binarize_image
import numpy as np
import cv2

class TestBinarizeImage(unittest.TestCase):
    def test_binarize_image_default_threshold(self):
        # Create a sample grayscale image
        sample_image = np.array([[0, 64], [127, 192]], dtype=np.uint8)
        
        # Expected output with default threshold of 128
        expected_output = np.array([[0, 0], [0, 255]], dtype=np.uint8)
        
        # Call the function
        result = binarize_image(sample_image)
        
        # Check if the result matches the expected output
        self.assertTrue(np.array_equal(result, expected_output))

    def test_binarize_image_custom_threshold(self):
        # Create a sample grayscale image
        sample_image = np.array([[0, 64], [127, 192]], dtype=np.uint8)
        
        # Custom threshold value
        custom_threshold = 64
        
        # Expected output with custom threshold of 64
        expected_output = np.array([[0, 255], [255, 255]], dtype=np.uint8)
        
        # Call the function with custom threshold
        result = binarize_image(sample_image, custom_threshold)
        
        # Check if the result matches the expected output
        self.assertTrue(np.array_equal(result, expected_output))

if __name__ == '__main__':
    unittest.main()