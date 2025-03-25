import unittest
from compute_gradient_magnitude import compute_gradient_magnitude
import cv2
import numpy as np

class TestComputeGradientMagnitude(unittest.TestCase):
    def test_compute_gradient_magnitude(self):
        # Load a sample image
        image_path = 'path_to_sample_image.jpg'
        
        # Call the function
        gradient_magnitude = compute_gradient_magnitude(image_path)
        
        # Check if the output is a 2D numpy array
        self.assertIsInstance(gradient_magnitude, np.ndarray)
        self.assertEqual(len(gradient_magnitude.shape), 2)
        
        # Check if the shape of the output matches the input image
        input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.assertEqual(gradient_magnitude.shape, input_image.shape)
        
        # Check if the gradient magnitude values are non-negative
        self.assertTrue((gradient_magnitude >= 0).all())

if __name__ == '__main__':
    unittest.main()