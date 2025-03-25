import unittest
from process_image import process_image
import cv2
import os
import numpy as np

class TestProcessImage(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.original_image = cv2.imread(self.test_image_path)

    def test_process_image(self):
        process_image(self.test_image_path)
        
        # Check if the output images are created
        self.assertTrue(os.path.exists("harris_original.png"))
        self.assertTrue(os.path.exists("harris_transformed.png"))
        
        # Load the processed images
        harris_original = cv2.imread("harris_original.png")
        harris_transformed = cv2.imread("harris_transformed.png")
        
        # Check if the dimensions match the original image
        self.assertEqual(harris_original.shape, self.original_image.shape)
        self.assertEqual(harris_transformed.shape, self.original_image.shape)
        
        # Check if the images have been modified (corners detected)
        self.assertNotEqual(np.sum(harris_original), np.sum(self.original_image))
        self.assertNotEqual(np.sum(harris_transformed), np.sum(self.original_image))

if __name__ == "__main__":
    unittest.main()