import unittest
from convert_image_to_yuv import convert_image_to_yuv
from PIL import Image
import os

class TestConvertImageToYUV(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_image.png"
        self.output_image_path = "yuv_image.png"

    def test_convert_image_to_yuv(self):
        # Create a test image in RGB mode
        test_image = Image.new("RGB", (100, 100), color="red")
        test_image.save(self.input_image_path)

        # Call the function to convert the image to YUV
        convert_image_to_yuv(self.input_image_path, self.output_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the output image and check its color mode
        output_image = Image.open(self.output_image_path)
        self.assertEqual(output_image.mode, "RGB")

if __name__ == "__main__":
    unittest.main()