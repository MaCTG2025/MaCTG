import unittest
from draw_ellipse_on_image import draw_ellipse_on_image
import cv2
import numpy as np
import os

class TestDrawEllipseOnImage(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "./test_image.png"
        self.output_image_path = "./output_image.png"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_draw_ellipse_on_image(self):
        # Create a test image
        test_image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.imwrite(self.input_image_path, test_image)

        # Call the function
        draw_ellipse_on_image(self.input_image_path, self.output_image_path)

        # Read the output image
        output_image = cv2.imread(self.output_image_path)

        # Check if the image has been modified
        self.assertNotEqual(np.sum(test_image), np.sum(output_image))

if __name__ == "__main__":
    unittest.main()