import unittest
from apply_oil_painting_effect import apply_oil_painting_effect
from PIL import Image

class TestApplyOilPaintingEffect(unittest.TestCase):
    def test_apply_oil_painting_effect(self):
        input_image_path = "test_input.jpg"
        output_image_path = "test_output.jpg"

        # Create a sample input image
        sample_image = Image.new("RGB", (100, 100), color="white")
        sample_image.save(input_image_path)

        # Call the function under test
        apply_oil_painting_effect(input_image_path, output_image_path)

        # Load the output image
        output_image = Image.open(output_image_path)

        # Check if the output image has the correct size
        self.assertEqual(output_image.size, (100, 100))

        # Clean up the test files
        sample_image.close()
        output_image.close()

if __name__ == "__main__":
    unittest.main()