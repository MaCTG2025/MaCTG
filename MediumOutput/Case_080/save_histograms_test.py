import unittest
from save_histograms import save_histograms
import numpy as np
import os

class TestSaveHistograms(unittest.TestCase):

    def test_save_histograms(self):
        # Create sample histograms
        original_hist = np.array([10, 20, 30, 40, 50], dtype=int)
        equalized_hist = np.array([5, 15, 25, 35, 45], dtype=int)

        # Define the output directory
        output_dir = "test_output"

        # Call the function to save histograms
        save_histograms(original_hist, equalized_hist, output_dir)

        # Check if the files were created successfully
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'original_histogram.npy')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'equalized_histogram.npy')))

        # Load the saved histograms and check their values
        saved_original_hist = np.load(os.path.join(output_dir, 'original_histogram.npy'))
        saved_equalized_hist = np.load(os.path.join(output_dir, 'equalized_histogram.npy'))

        self.assertTrue(np.array_equal(saved_original_hist, original_hist))
        self.assertTrue(np.array_equal(saved_equalized_hist, equalized_hist))

if __name__ == '__main__':
    unittest.main()