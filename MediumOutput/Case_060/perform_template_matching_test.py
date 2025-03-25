import unittest
from perform_template_matching import perform_template_matching
import cv2
import numpy as np

class TestPerformTemplateMatching(unittest.TestCase):
    def setUp(self):
        # Load the brightened image and template for testing
        self.brightened_image = cv2.imread("./test_brightened_image.jpg", 0)
        self.template_path = "./template.jpg"
        
        # Ensure the images are loaded successfully
        if self.brightened_image is None:
            raise FileNotFoundError("Brightened image not found or unable to read.")
        if cv2.imread(self.template_path, 0) is None:
            raise FileNotFoundError("Template image not found or unable to read.")

    def test_perform_template_matching(self):
        result = perform_template_matching(self.brightened_image, self.template_path)
        
        # Check if the result is a tuple of 4 integers
        self.assertEqual(len(result), 4)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertIsInstance(result[3], int)
        
        # Check if the matched region is within the bounds of the brightened image
        self.assertTrue(0 <= result[0] < self.brightened_image.shape[1])  # x
        self.assertTrue(0 <= result[1] < self.brightened_image.shape[0])  # y
        self.assertTrue(result[2] > 0 and result[3] > 0)  # width and height

if __name__ == '__main__':
    unittest.main()