import unittest
from save_output_image import save_output_image
import numpy as np
import os

class TestSaveOutputImage(unittest.TestCase):
    def setUp(self):
        self.overlay_image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.output_path = "test_output.png"

    def test_save_output_image_valid_path(self):
        save_output_image(self.overlay_image, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_save_output_image_invalid_path(self):
        invalid_path = "/path/that/does/not/exist/test_output.png"
        with self.assertRaises(Exception):
            save_output_image(self.overlay_image, invalid_path)

if __name__ == "__main__":
    unittest.main()