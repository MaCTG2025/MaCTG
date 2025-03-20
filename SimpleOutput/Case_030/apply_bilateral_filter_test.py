import unittest
from apply_bilateral_filter import apply_bilateral_filter
import cv2
import os

class TestApplyBilateralFilter(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.output_image_path = "test_output.jpg"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_apply_bilateral_filter(self):
        # Create a sample input image
        sample_image = cv2.imread("sample_input.jpg")
        cv2.imwrite(self.input_image_path, sample_image)

        # Call the function
        apply_bilateral_filter(self.input_image_path, self.output_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the output image and check its dimensions
        output_image = cv2.imread(self.output_image_path)
        self.assertIsNotNone(output_image)
        self.assertEqual(output_image.shape, sample_image.shape)

if __name__ == "__main__":
    unittest.main()