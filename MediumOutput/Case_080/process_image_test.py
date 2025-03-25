import unittest
from process_image import process_image
import numpy as np
import cv2

class TestProcessImage(unittest.TestCase):
    def setUp(self):
        self.image_path = 'path_to_your_test_image.jpg'  # Replace with the actual path to your test image

    def test_process_image(self):
        # Call the function with the test image path
        gray_image, equalized_image, original_hist, equalized_hist = process_image(self.image_path)

        # Check if the images are of the correct type and shape
        self.assertIsInstance(gray_image, np.ndarray)
        self.assertEqual(gray_image.dtype, np.uint8)  # Ensure the grayscale image is of type uint8

        self.assertIsInstance(equalized_image, np.ndarray)
        self.assertEqual(equalized_image.dtype, np.uint8)  # Ensure the equalized image is of type uint8

        # Check if the histograms are of the correct type and shape
        self.assertIsInstance(original_hist, np.ndarray)
        self.assertEqual(original_hist.shape, (256, 1))  # Ensure the histogram has the correct shape

        self.assertIsInstance(equalized_hist, np.ndarray)
        self.assertEqual(equalized_hist.shape, (256, 1))  # Ensure the histogram has the correct shape

        # Optionally, you can add more specific checks to verify the correctness of the processed images and histograms

if __name__ == '__main__':
    unittest.main()