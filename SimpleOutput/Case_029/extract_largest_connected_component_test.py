import unittest
from extract_largest_connected_component import extract_largest_connected_component
import cv2
import numpy as np

class TestExtractLargestConnectedComponent(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.png"
        self.expected_output_path = "expected_output.png"

    def test_extract_largest_connected_component(self):
        # Create a test image with known properties
        test_image = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(test_image, (20, 20), (80, 80), 255, -1)  # White rectangle
        cv2.circle(test_image, (50, 50), 30, 255, -1)         # White circle
        cv2.imwrite(self.test_image_path, test_image)

        # Call the function under test
        extract_largest_connected_component(self.test_image_path)

        # Load the expected output image
        expected_output = cv2.imread(self.expected_output_path)

        # Load the actual output image
        actual_output = cv2.imread("largest_connected_component.png")

        # Compare the two images
        self.assertTrue(np.array_equal(expected_output, actual_output))

if __name__ == "__main__":
    unittest.main()