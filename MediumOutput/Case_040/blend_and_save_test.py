import unittest
from blend_and_save import blend_and_save
import numpy as np
import os

class TestBlendAndSave(unittest.TestCase):
    def setUp(self):
        self.stylized_image = np.ones((100, 100, 3), dtype=np.uint8) * 255
        self.edges = np.zeros((100, 100, 3), dtype=np.uint8)
        self.output_path = 'test_output.png'

    def test_blending_weights_sum_to_one(self):
        with self.assertRaises(AssertionError):
            blend_and_save(self.stylized_image, self.edges, 0.7, 0.4, self.output_path)

    def test_valid_input_images(self):
        blend_and_save(self.stylized_image, self.edges, 0.7, 0.3, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_negative_weights(self):
        with self.assertRaises(AssertionError):
            blend_and_save(self.stylized_image, self.edges, -0.1, 1.1, self.output_path)

if __name__ == '__main__':
    unittest.main()