import unittest
from detect_blobs import detect_blobs
import cv2
import numpy as np

class TestDetectBlobs(unittest.TestCase):
    def test_detect_blobs(self):
        # Path to the test image
        image_path = 'test_image.jpg'
        
        # Expected output
        expected_blobs = [(100, 100, 400), (200, 200, 900)]
        expected_image_shape = (300, 300, 3)
        
        # Call the function
        blobs, image = detect_blobs(image_path)
        
        # Check if the returned blobs match the expected ones
        self.assertEqual(blobs, expected_blobs)
        
        # Check if the returned image has the correct shape
        self.assertEqual(image.shape, expected_image_shape)

if __name__ == '__main__':
    unittest.main()