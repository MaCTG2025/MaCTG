import unittest
from template_matching_with_noise import template_matching_with_noise
import cv2
import numpy as np
import os

class TestTemplateMatchingWithNoise(unittest.TestCase):
    def test_template_matching_with_noise(self):
        # Define test parameters
        input_image_path = "test_input.jpg"
        template_image_path = "test_template.jpg"
        output_image_path = "test_output.jpg"
        sigma = 1.0
        mean = 0.0
        rectangle_thickness = 2

        # Create test images
        input_image = np.zeros((100, 100, 3), dtype=np.uint8)
        template_image = np.zeros((50, 50, 3), dtype=np.uint8)
        input_image[25:75, 25:75] = [255, 255, 255]
        template_image[10:40, 10:40] = [255, 255, 255]

        # Save test images
        cv2.imwrite(input_image_path, input_image)
        cv2.imwrite(template_image_path, template_image)

        # Call the function
        template_matching_with_noise(input_image_path, template_image_path, output_image_path, sigma, mean, rectangle_thickness)

        # Load the output image
        output_image = cv2.imread(output_image_path)

        # Check if the rectangle is drawn correctly
        expected_top_left = (25, 25)
        expected_bottom_right = (75, 75)
        actual_top_left = tuple(output_image[expected_top_left[1], expected_top_left[0]])
        actual_bottom_right = tuple(output_image[expected_bottom_right[1], expected_bottom_right[0]])

        self.assertEqual(actual_top_left, (0, 0, 255))
        self.assertEqual(actual_bottom_right, (0, 0, 255))

        # Clean up test files
        os.remove(input_image_path)
        os.remove(template_image_path)
        os.remove(output_image_path)

if __name__ == "__main__":
    unittest.main()