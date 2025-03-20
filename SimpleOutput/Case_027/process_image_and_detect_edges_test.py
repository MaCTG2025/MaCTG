import unittest
from process_image_and_detect_edges import process_image_and_detect_edges
import cv2
import os

class TestProcessImageAndDetectEdges(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "./test_image.png"
        self.output_image_path = "./output_edge_map.png"
        self.kernel_size = 3

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_process_image_and_detect_edges(self):
        # Call the function with the test inputs
        process_image_and_detect_edges(self.input_image_path, self.output_image_path, self.kernel_size)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the output image and check its dimensions
        output_image = cv2.imread(self.output_image_path)
        self.assertIsNotNone(output_image)
        self.assertEqual(output_image.shape[:2], (480, 640))  # Assuming the input image has these dimensions

if __name__ == '__main__':
    unittest.main()