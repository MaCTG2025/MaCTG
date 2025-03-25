import unittest
from harris_corner_detection import harris_corner_detection
import numpy as np
import cv2

class TestHarrisCornerDetection(unittest.TestCase):
    def test_harris_corner_detection(self):
        # Create a sample image (black image with a white square in the center)
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        image[40:60, 40:60] = [255, 255, 255]  # White square

        # Call the function with default parameters
        result_image_default = harris_corner_detection(image)
        
        # Check if the result image has the same dimensions as the input image
        self.assertEqual(result_image_default.shape, image.shape)
        
        # Call the function with custom parameters
        result_image_custom = harris_corner_detection(image, block_size=3, ksize=5)
        
        # Check if the result image has the same dimensions as the input image
        self.assertEqual(result_image_custom.shape, image.shape)
        
        # Check if the function raises ValueError for invalid block_size
        with self.assertRaises(ValueError):
            harris_corner_detection(image, block_size=-1)
        
        # Check if the function raises ValueError for invalid ksize
        with self.assertRaises(ValueError):
            harris_corner_detection(image, ksize=-1)

if __name__ == '__main__':
    unittest.main()