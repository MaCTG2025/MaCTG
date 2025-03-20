import unittest
from apply_sharpening_filter import apply_sharpening_filter
from PIL import Image

class TestApplySharpeningFilter(unittest.TestCase):
    def test_apply_sharpening_filter(self):
        input_image_path = 'test_input.jpg'
        output_image_path = 'test_output.jpg'

        # Create a sample image for testing
        sample_image = Image.new('RGB', (100, 100), color='white')
        sample_image.save(input_image_path)

        apply_sharpening_filter(input_image_path, output_image_path)
        self.assertTrue(os.path.exists(output_image_path))
        sharpened_image = Image.open(output_image_path)
        self.assertEqual(sharpened_image.size, (100, 100))

if __name__ == '__main__':
    unittest.main()