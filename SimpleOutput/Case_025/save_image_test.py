import unittest
from save_image import save_image
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    def test_save_image(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Define the output path
        output_path = "test_output.png"
        
        # Call the function to save the image
        save_image(sample_image, output_path)
        
        # Check if the file exists at the specified path
        self.assertTrue(os.path.exists(output_path))

if __name__ == "__main__":
    unittest.main()