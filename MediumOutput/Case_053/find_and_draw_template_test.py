import unittest
from find_and_draw_template import find_and_draw_template
import cv2
import numpy as np
import os

class TestFindAndDrawTemplate(unittest.TestCase):

    def test_find_and_draw_template(self):
        # Load images
        main_image_path = 'path_to_main_image.jpg'
        template_image_path = 'path_to_template_image.jpg'

        # Define test parameters
        angles = [0, 45, 90, 135]
        rectangle_thickness = 2

        # Call the function
        result_image = find_and_draw_template(main_image_path, template_image_path, angles, rectangle_thickness)

        # Check if the result image is not empty
        self.assertIsNotNone(result_image)

        # Check if the result image has the correct dimensions
        expected_height, expected_width = cv2.imread(main_image_path).shape[:2]
        actual_height, actual_width = result_image.shape[:2]
        self.assertEqual(actual_height, expected_height)
        self.assertEqual(actual_width, expected_width)

        # Check if the output file is saved correctly
        self.assertTrue(os.path.exists("wheres_waldo_found.png"))

if __name__ == '__main__':
    unittest.main()