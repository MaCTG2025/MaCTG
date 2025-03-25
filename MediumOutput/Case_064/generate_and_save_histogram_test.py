import unittest
from generate_and_save_histogram import generate_and_save_histogram
import numpy as np
import os

class TestGenerateAndSaveHistogram(unittest.TestCase):
    def setUp(self):
        self.image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
        self.output_path = "test_hist.npy"

    def test_generate_and_save_histogram_valid_image(self):
        generate_and_save_histogram(self.image, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        loaded_histograms = np.load(self.output_path)
        self.assertEqual(len(loaded_histograms), 3)
        for histogram in loaded_histograms:
            self.assertEqual(histogram.shape, (256,))

    def test_generate_and_save_histogram_invalid_output_path(self):
        # The function should handle invalid paths gracefully and not raise an exception
        invalid_path = "/invalid/path/test_hist.npy"
        generate_and_save_histogram(self.image, invalid_path)
        self.assertFalse(os.path.exists(invalid_path))

if __name__ == "__main__":
    unittest.main()