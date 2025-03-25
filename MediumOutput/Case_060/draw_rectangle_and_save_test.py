import unittest
from draw_rectangle_and_save import draw_rectangle_and_save
import numpy as np
import os

class TestDrawRectangleAndSave(unittest.TestCase):
    def setUp(self):
        self.brightened_image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.matched_region = (20, 30, 40, 50)
        self.output_path = "test_output.png"

    def test_draw_rectangle_and_save_valid_input(self):
        draw_rectangle_and_save(self.brightened_image, self.matched_region, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_draw_rectangle_and_save_invalid_output_path(self):
        invalid_output_path = "/path/to/nonexistent/directory/test_output.png"
        with self.assertRaises(FileNotFoundError):
            draw_rectangle_and_save(self.brightened_image, self.matched_region, invalid_output_path)

if __name__ == "__main__":
    unittest.main()