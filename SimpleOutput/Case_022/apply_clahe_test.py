import unittest
from apply_clahe import apply_clahe
import os

class TestApplyCLAHE(unittest.TestCase):
    def setUp(self):
        self.input_image_path = 'test_image.png'
        self.output_image_path = 'clahe_image.png'

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_apply_clahe_valid_input(self):
        apply_clahe(self.input_image_path, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_apply_clahe_invalid_input_path(self):
        with self.assertRaises(ValueError):
            apply_clahe('nonexistent_image.png', self.output_image_path)

    def test_apply_clahe_invalid_output_path(self):
        with self.assertRaises(Exception):
            apply_clahe(self.input_image_path, '/invalid/path/clahe_image.png')

if __name__ == '__main__':
    unittest.main()