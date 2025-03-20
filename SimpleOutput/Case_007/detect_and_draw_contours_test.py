import unittest
from detect_and_draw_contours import detect_and_draw_contours
import numpy as np
import os
import cv2

class TestDetectAndDrawContours(unittest.TestCase):
    def setUp(self):
        self.binary_image = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(self.binary_image, (30, 30), (70, 70), 255, -1)
        self.output_path = "test_output.png"
        self.color = (0, 0, 255)
        self.thickness = 2

    def test_detect_and_draw_contours(self):
        result_image = detect_and_draw_contours(self.binary_image, self.output_path, self.color, self.thickness)
        
        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_path))
        
        # Load the saved image and check its dimensions
        loaded_image = cv2.imread(self.output_path)
        self.assertEqual(loaded_image.shape, (100, 100, 3))
        
        # Check if the contours are drawn correctly
        contours, _ = cv2.findContours(result_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.assertEqual(len(contours), 1)
        x, y, w, h = cv2.boundingRect(contours[0])
        self.assertEqual(x, 30)
        self.assertEqual(y, 30)
        self.assertEqual(w, 40)
        self.assertEqual(h, 40)

if __name__ == '__main__':
    unittest.main()