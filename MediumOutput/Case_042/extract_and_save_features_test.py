import unittest
from extract_and_save_features import extract_and_save_features
import numpy as np
from skimage.io import imread, imsave
import os

class TestExtractAndSaveFeatures(unittest.TestCase):
    def test_extract_and_save_features(self):
        # Create a test image
        test_image = np.array([
            [0, 0, 0, 255],
            [0, 255, 255, 255],
            [255, 255, 0, 0],
            [255, 0, 0, 0]
        ], dtype=np.uint8)
        
        # Save the test image temporarily
        test_image_path = "test_image.png"
        imsave(test_image_path, test_image)
        
        # Call the function with default parameters
        extract_and_save_features(test_image_path)
        
        # Load the saved HOG and LBP features
        hog_features = np.load("hog_features.npy")
        lbp_features = np.load("lbp_features.npy")
        
        # Check if the shapes of the features are correct
        self.assertEqual(hog_features.shape, (64,))
        self.assertEqual(lbp_features.shape, (32,))
        
        # Clean up the temporary test image and feature files
        os.remove(test_image_path)
        os.remove("hog_features.npy")
        os.remove("lbp_features.npy")

if __name__ == "__main__":
    unittest.main()