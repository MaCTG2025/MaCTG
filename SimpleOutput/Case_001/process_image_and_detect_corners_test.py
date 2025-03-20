import unittest
from process_image_and_detect_corners import process_image_and_detect_corners
import cv2
import numpy as np

class TestProcessImageAndDetectCorners(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.jpg"
        self.output_image_path = "output_test_image.png"
        # Create a test image with known corners for testing
        self.create_test_image()

    def create_test_image(self):
        # Create a blank image
        self.img = np.zeros((200, 200, 3), dtype=np.uint8)
        # Draw two squares with known corners
        cv2.rectangle(self.img, (50, 50), (100, 100), (255, 255, 255), -1)
        cv2.rectangle(self.img, (150, 150), (200, 200), (255, 255, 255), -1)
        # Save the test image
        cv2.imwrite(self.test_image_path, self.img)

    def test_process_image_and_detect_corners(self):
        # Process the test image
        process_image_and_detect_corners(self.test_image_path, self.output_image_path)
        
        # Load the processed image
        processed_img = cv2.imread(self.output_image_path)
        
        # Check if the corners are detected correctly
        red_pixels = np.sum(processed_img == [0, 0, 255])
        self.assertGreater(red_pixels, 0, "No corners were detected.")

if __name__ == "__main__":
    unittest.main()