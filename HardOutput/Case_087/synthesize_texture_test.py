import unittest
from synthesize_texture import synthesize_texture
from PIL import Image
import os

class TestSynthesizeTexture(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.output_image_path = "test_output.png"
        self.output_size = (64, 64)

        # Create a sample input image
        input_image = Image.new("RGB", (32, 32), color="red")
        input_image.save(self.input_image_path)

    def test_synthesize_texture(self):
        # Call the function to synthesize texture
        synthesize_texture(self.input_image_path, self.output_image_path, self.output_size)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Open the output image and check its dimensions
        output_image = Image.open(self.output_image_path)
        self.assertEqual(output_image.size, self.output_size)

        # Check if the output image has the correct number of channels
        self.assertEqual(output_image.mode, "RGB")

if __name__ == "__main__":
    unittest.main()