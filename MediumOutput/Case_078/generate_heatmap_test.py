import unittest
from generate_heatmap import generate_heatmap
import numpy as np
import os

class TestGenerateHeatmap(unittest.TestCase):

    def test_valid_difference_array(self):
        difference = np.random.rand(10, 10)
        output_path = "test_heatmap.png"
        generate_heatmap(difference, output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_invalid_difference_array(self):
        with self.assertRaises(ValueError):
            generate_heatmap("not_an_array", "output.png")

    def test_ioerror_output_path(self):
        with self.assertRaises(IOError):
            generate_heatmap(np.random.rand(10, 10), "/invalid/path/output.png")

if __name__ == '__main__':
    unittest.main()