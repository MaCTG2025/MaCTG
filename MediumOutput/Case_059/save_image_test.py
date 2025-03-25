import unittest
from save_image import save_image
import numpy as np
from PIL import Image
import os

class TestSaveImage(unittest.TestCase):

    def test_valid_image(self):
        # Create a sample segmented image
        segmented_image = np.zeros((100, 100, 3), dtype=np.uint8)
        output_path = "test_output.png"
        
        # Call the function
        save_image(segmented_image, output_path)
        
        # Check if the file exists
        self.assertTrue(os.path.exists(output_path))
        
        # Clean up
        os.remove(output_path)

    def test_invalid_image_type(self):
        # Create an invalid image type
        invalid_image = "not_an_array"
        output_path = "test_output.png"
        
        # Expect a ValueError
        with self.assertRaises(ValueError):
            save_image(invalid_image, output_path)

    def test_io_error(self):
        # Create a sample segmented image
        segmented_image = np.zeros((100, 100, 3), dtype=np.uint8)
        output_path = "/nonexistent_directory/test_output.png"
        
        # Expect an IOError
        with self.assertRaises(IOError):
            save_image(segmented_image, output_path)

if __name__ == '__main__':
    unittest.main()