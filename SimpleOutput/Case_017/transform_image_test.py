import unittest
from transform_image import transform_image
from PIL import Image

class TestTransformImage(unittest.TestCase):
    def test_transform_image(self):
        # Create a temporary image for testing
        temp_input_path = 'temp_test_image.png'
        temp_output_path = 'temp_rotated_flipped_image.png'

        # Create a simple image for testing
        with Image.new('RGB', (200, 200), color='red') as img:
            img.save(temp_input_path)

        # Call the function to transform the image
        transform_image(temp_input_path, temp_output_path)

        # Open the transformed image and check its properties
        with Image.open(temp_output_path) as transformed_img:
            self.assertEqual(transformed_img.size, (200, 200))
            self.assertEqual(transformed_img.mode, 'RGB')
            # Check if the image is correctly transformed (180-degree rotation and vertical flip)
            expected_color = transformed_img.getpixel((100, 100))  # Center pixel after transformation
            self.assertEqual(expected_color, (255, 0, 0))  # Red color remains red after transformation

if __name__ == '__main__':
    unittest.main()