import unittest
from apply_image_arithmetic_operations import apply_image_arithmetic_operations
from PIL import Image
import os

class TestApplyImageArithmeticOperations(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "./test_image.png"
        self.value = 100

    def test_apply_image_arithmetic_operations(self):
        # Create a test image
        test_img = Image.new('L', (100, 100), color=150)
        test_img.save(self.test_image_path)

        # Call the function
        added_image_path, subtracted_image_path = apply_image_arithmetic_operations(self.test_image_path, self.value)

        # Check if the files were created
        self.assertTrue(os.path.exists(added_image_path))
        self.assertTrue(os.path.exists(subtracted_image_path))

        # Load the images and check their pixel values
        added_img = Image.open(added_image_path)
        subtracted_img = Image.open(subtracted_image_path)

        for x in range(100):
            for y in range(100):
                added_pixel_value = added_img.getpixel((x, y))
                subtracted_pixel_value = subtracted_img.getpixel((x, y))
                expected_added_value = min(255, 150 + self.value)
                expected_subtracted_value = max(0, 150 - self.value)
                self.assertEqual(added_pixel_value, expected_added_value)
                self.assertEqual(subtracted_pixel_value, expected_subtracted_value)

if __name__ == '__main__':
    unittest.main()