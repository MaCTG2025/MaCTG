import unittest
from process_image import process_image
import cv2
import os

class TestProcessImage(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "./test_image.png"
        self.output_image_path = "./binary_image.png"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_process_image_with_default_parameters(self):
        process_image(self.input_image_path, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))
        binary_image = cv2.imread(self.output_image_path, cv2.IMREAD_GRAYSCALE)
        self.assertIsNotNone(binary_image)
        self.assertEqual(binary_image.shape[0], cv2.imread(self.input_image_path).shape[0])
        self.assertEqual(binary_image.shape[1], cv2.imread(self.input_image_path).shape[1])

    def test_process_image_with_custom_block_size_and_C(self):
        block_size = 7
        C = 5
        process_image(self.input_image_path, self.output_image_path, block_size, C)
        self.assertTrue(os.path.exists(self.output_image_path))
        binary_image = cv2.imread(self.output_image_path, cv2.IMREAD_GRAYSCALE)
        self.assertIsNotNone(binary_image)
        self.assertEqual(binary_image.shape[0], cv2.imread(self.input_image_path).shape[0])
        self.assertEqual(binary_image.shape[1], cv2.imread(self.input_image_path).shape[1])

if __name__ == "__main__":
    unittest.main()