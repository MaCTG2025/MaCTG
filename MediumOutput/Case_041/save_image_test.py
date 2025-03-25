import unittest
from save_image import save_image
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    def test_save_image_valid_input(self):
        # Create a sample image
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Define the output path
        output_path = "test_output_image.png"
        
        # Call the function
        save_image(image, output_path)
        
        # Check if the file exists
        self.assertTrue(os.path.exists(output_path))
        
        # Clean up the file
        os.remove(output_path)

if __name__ == "__main__":
    unittest.main()