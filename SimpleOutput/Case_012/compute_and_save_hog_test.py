import unittest
from compute_and_save_hog import compute_and_save_hog
import numpy as np
from skimage import io

class TestComputeAndSaveHOG(unittest.TestCase):
    def test_compute_and_save_hog(self):
        # Define test parameters
        image_path = "./test_image.png"
        cell_size = (8, 8)
        block_size = (2, 2)
        nbins = 9
        output_path = "hog_test.npy"

        # Call the function with test parameters
        compute_and_save_hog(image_path, cell_size, block_size, nbins, output_path)

        # Check if the output file exists
        self.assertTrue(io.exists(output_path))

        # Load the saved HOG features
        hog_features = np.load(output_path)

        # Check if the loaded HOG features have the expected shape
        expected_shape = (int(np.prod(cell_size) * np.prod(block_size)), nbins)
        self.assertEqual(hog_features.shape, expected_shape)

if __name__ == "__main__":
    unittest.main()