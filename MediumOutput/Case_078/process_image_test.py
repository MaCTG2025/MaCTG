import unittest
from process_image import process_image
import os

class TestProcessImage(unittest.TestCase):
    def setUp(self):
        self.test_image_path = 'test_image.jpg'
        self.output_path = 'output_heatmap.jpg'

    def test_process_image(self):
        try:
            process_image(self.test_image_path, self.output_path)
            self.assertTrue(os.path.exists(self.output_path))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

if __name__ == '__main__':
    unittest.main()