import unittest
from image_processing_pipeline import image_processing_pipeline
import os
import numpy as np
import cv2

class TestImageProcessingPipeline(unittest.TestCase):
    def setUp(self):
        self.test_image_path = 'test_image.jpg'
        self.output_image_path = 'output_image.jpg'
        self.mean = 0.0
        self.std_dev = 1.0
        self.kernel_size = 3
        
        # Create a test image
        self.test_image = np.zeros((100, 100), dtype=np.uint8)
        cv2.circle(self.test_image, (50, 50), 20, 255, -1)
        
        # Save the test image
        cv2.imwrite(self.test_image_path, self.test_image)

    def tearDown(self):
        # Remove the test image and output image after each test
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_valid_input(self):
        image_processing_pipeline(self.test_image_path, self.mean, self.std_dev, self.kernel_size, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_invalid_mean(self):
        with self.assertRaises(ValueError):
            image_processing_pipeline(self.test_image_path, 'invalid_mean', self.std_dev, self.kernel_size, self.output_image_path)

    def test_invalid_std_dev(self):
        with self.assertRaises(ValueError):
            image_processing_pipeline(self.test_image_path, self.mean, 'invalid_std_dev', self.kernel_size, self.output_image_path)

    def test_even_kernel_size(self):
        with self.assertRaises(ValueError):
            image_processing_pipeline(self.test_image_path, self.mean, self.std_dev, 2, self.output_image_path)

    def test_non_integer_kernel_size(self):
        with self.assertRaises(ValueError):
            image_processing_pipeline(self.test_image_path, self.mean, self.std_dev, 3.5, self.output_image_path)

    def test_invalid_output_path(self):
        with self.assertRaises(ValueError):
            image_processing_pipeline(self.test_image_path, self.mean, self.std_dev, self.kernel_size, 'invalid_output_path')

if __name__ == '__main__':
    unittest.main()