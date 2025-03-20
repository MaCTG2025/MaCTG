import unittest
from denoise_image import denoise_image
import os

class TestDenoiseImage(unittest.TestCase):
    def test_denoise_image(self):
        input_image_path = 'path/to/test_image.png'
        output_image_path = 'path/to/denoised_image.png'

        # Ensure the input image exists
        if not os.path.exists(input_image_path):
            self.skipTest(f"Input image file {input_image_path} does not exist.")

        # Call the function
        denoise_image(input_image_path, output_image_path)

        # Verify the output image was created
        self.assertTrue(os.path.exists(output_image_path))

if __name__ == '__main__':
    unittest.main()