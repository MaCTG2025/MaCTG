import unittest
from save_segmented_image import save_segmented_image
import numpy as np
import os
import cv2

class TestSaveSegmentedImage(unittest.TestCase):
    def test_save_segmented_image(self):
        # Create a sample segmented image
        segmented_image = np.zeros((100, 100, 3), dtype=np.uint8)
        segmented_image[30:70, 30:70] = [255, 255, 255]  # White square in the center
        
        # Define the output path
        output_path = "test_output.png"
        
        # Call the function to save the image
        save_segmented_image(segmented_image, output_path)
        
        # Check if the file exists
        self.assertTrue(os.path.exists(output_path))
        
        # Read the saved image using OpenCV
        saved_image = cv2.imread(output_path)
        
        # Check if the saved image has the same dimensions as the original
        self.assertEqual(saved_image.shape, segmented_image.shape)

if __name__ == "__main__":
    unittest.main()