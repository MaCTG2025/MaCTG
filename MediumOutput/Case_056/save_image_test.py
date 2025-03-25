import unittest
from save_image import save_image
import cv2
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    def test_save_image(self):
        # Create a sample processed image
        processed_image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Define an output path
        output_path = "test_output.png"
        
        # Call the function to save the image
        save_image(processed_image, output_path)
        
        # Check if the file exists at the specified path
        self.assertTrue(os.path.exists(output_path))
        
        # Read the saved image using OpenCV
        saved_image = cv2.imread(output_path)
        
        # Check if the saved image has the same shape as the processed image
        self.assertEqual(saved_image.shape, processed_image.shape)
        
        # Clean up the saved file
        os.remove(output_path)

if __name__ == "__main__":
    unittest.main()