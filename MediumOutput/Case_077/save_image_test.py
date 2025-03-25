import unittest
from save_image import save_image
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    def test_save_image_valid(self):
        # Create a sample image
        sample_image = np.zeros((100, 100), dtype=np.uint8)
        
        # Define an output path
        output_path = "test_output.png"
        
        # Call the function
        save_image(sample_image, output_path)
        
        # Check if the file exists
        self.assertTrue(os.path.exists(output_path))
        
        # Clean up
        os.remove(output_path)

    def test_save_image_invalid_format(self):
        # Create a sample image
        sample_image = np.zeros((100, 100), dtype=np.uint8)
        
        # Define an invalid output path
        output_path = "test_output.txt"
        
        # Call the function and check if the error message is printed
        with self.assertLogs(level='INFO') as log:
            save_image(sample_image, output_path)
        self.assertIn("Error saving image", log.output[0])

if __name__ == '__main__':
    unittest.main()