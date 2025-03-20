import unittest
from match_and_draw_contours import match_and_draw_contours
import cv2
import numpy as np

class TestMatchAndDrawContours(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.template_image_path = "test_template.jpg"
        self.output_image_path = "test_output.jpg"

        # Create test images
        self.create_test_images()

    def create_test_images(self):
        # Create a simple input image with a white square
        input_image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.rectangle(input_image, (50, 50), (150, 150), (255, 255, 255), -1)
        cv2.imwrite(self.input_image_path, input_image)

        # Create a template image with a smaller white square
        template_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(template_image, (25, 25), (75, 75), (255, 255, 255), -1)
        cv2.imwrite(self.template_image_path, template_image)

    def test_match_and_draw_contours(self):
        # Call the function
        match_and_draw_contours(self.input_image_path, self.template_image_path, self.output_image_path)

        # Load the output image
        output_image = cv2.imread(self.output_image_path)

        # Check if the rectangle is drawn correctly
        expected_top_left = (50, 50)
        expected_bottom_right = (150, 150)
        actual_top_left = tuple(np.argwhere(output_image[:, :, 0] == 0)[0])
        actual_bottom_right = tuple(np.argwhere(output_image[:, :, 0] == 0)[-1])

        self.assertEqual(actual_top_left, expected_top_left)
        self.assertEqual(actual_bottom_right, expected_bottom_right)

if __name__ == "__main__":
    unittest.main()