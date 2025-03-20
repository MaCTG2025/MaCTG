import unittest
from locate_and_draw_bounding_box import locate_and_draw_bounding_box
import os
import cv2
import numpy as np

class TestLocateAndDrawBoundingBox(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.template_image_path = "test_template.jpg"
        self.output_image_path = "test_output.jpg"

    def tearDown(self):
        if os.path.exists(self.input_image_path):
            os.remove(self.input_image_path)
        if os.path.exists(self.template_image_path):
            os.remove(self.template_image_path)
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_template_found(self):
        # Create a mock input image with the template inside it
        input_image = np.zeros((200, 200, 3), dtype=np.uint8)
        template_image = np.zeros((50, 50, 3), dtype=np.uint8)
        input_image[75:125, 75:125] = template_image
        cv2.imwrite(self.input_image_path, input_image)
        cv2.imwrite(self.template_image_path, template_image)

        # Call the function
        locate_and_draw_bounding_box(self.input_image_path, self.template_image_path, self.output_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Read the output image and check if the bounding box is drawn correctly
        output_image = cv2.imread(self.output_image_path)
        top_left = (75, 75)
        bottom_right = (125, 125)
        bounding_box_color = (0, 0, 255)
        bounding_box_thickness = 2
        self.assertEqual(output_image[top_left[1], top_left[0]], bounding_box_color)
        self.assertEqual(output_image[bottom_right[1], bottom_right[0]], bounding_box_color)

    def test_template_not_found(self):
        # Create a mock input image without the template
        input_image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.imwrite(self.input_image_path, input_image)
        cv2.imwrite(self.template_image_path, input_image)

        # Call the function
        locate_and_draw_bounding_box(self.input_image_path, self.template_image_path, self.output_image_path)

        # Check if the output image does not exist
        self.assertFalse(os.path.exists(self.output_image_path))

if __name__ == "__main__":
    unittest.main()