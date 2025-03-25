import unittest
from process_image import process_image
import cv2
import os

class TestProcessImage(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.png"
        self.expected_output_path = "canny_image.png"

    def test_process_image_exists(self):
        # Ensure the test image exists
        self.assertTrue(os.path.exists(self.test_image_path))

    def test_process_image_correctness(self):
        # Process the image
        process_image(self.test_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.expected_output_path))

        # Load the expected and actual images
        expected_image = cv2.imread("expected_canny_image.png")
        actual_image = cv2.imread(self.expected_output_path)

        # Compare the images
        self.assertTrue(cv2.norm(expected_image, actual_image, cv2.NORM_L2) == 0)

if __name__ == "__main__":
    unittest.main()