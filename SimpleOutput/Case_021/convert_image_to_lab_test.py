import unittest
from convert_image_to_lab import convert_image_to_lab
import os

class TestConvertImageToLab(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_image.png"
        self.output_image_path = "lab_image.png"

    def test_convert_image_to_lab(self):
        # Check if the input image exists
        self.assertTrue(os.path.exists(self.input_image_path))

        # Call the function to convert the image
        convert_image_to_lab(self.input_image_path, self.output_image_path)

        # Check if the output image was created
        self.assertTrue(os.path.exists(self.output_image_path))

        # Optionally, you can add more checks to verify the content of the output image
        # For example, check the shape of the image or specific pixel values

if __name__ == "__main__":
    unittest.main()