import unittest
from load_image import load_image
from PIL import Image

class TestLoadImage(unittest.TestCase):
    def test_load_valid_image(self):
        # Assuming 'test_image.jpg' exists in the same directory as this test file
        image = load_image('test_image.jpg')
        self.assertIsInstance(image, Image.Image)

    def test_load_nonexistent_image(self):
        with self.assertRaises(FileNotFoundError):
            load_image('nonexistent_image.jpg')

    def test_load_invalid_format(self):
        with self.assertRaises(ValueError):
            load_image('invalid_format.txt')

if __name__ == '__main__':
    unittest.main()