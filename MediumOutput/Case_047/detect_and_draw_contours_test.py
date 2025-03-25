import unittest
from detect_and_draw_contours import detect_and_draw_contours
import cv2
import numpy as np

class TestDetectAndDrawContours(unittest.TestCase):
    def test_detect_and_draw_contours(self):
        # Create a sample image with a simple contour
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(sample_image, (20, 20), (80, 80), (255, 255, 255), -1)

        # Define the output path for the test image
        output_path = "test_output.png"

        # Call the function with the sample image and output path
        detect_and_draw_contours(sample_image, output_path)

        # Load the output image to check if contours were drawn correctly
        output_image = cv2.imread(output_path)

        # Check if the output image has non-zero pixels at the expected contour positions
        self.assertTrue(np.any(output_image[20:80, 20:80] == [0, 0, 255]))

if __name__ == '__main__':
    unittest.main()