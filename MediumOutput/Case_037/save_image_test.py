import unittest
from save_image import save_image
import numpy as np
import os

class TestSaveImage(unittest.TestCase):

    def test_valid_image_and_path(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)

        # Define a valid output path
        output_path = 'test_output.png'

        # Call the function
        save_image(sample_image, output_path)

        # Check if the file exists
        self.assertTrue(os.path.exists(output_path))

        # Clean up the created file
        os.remove(output_path)

    def test_invalid_image_type(self):
        # Define an invalid image type
        invalid_image = "not_an_array"

        # Define a valid output path
        output_path = 'test_output.png'

        # Expect a cv2.error exception
        with self.assertRaises(cv2.error):
            save_image(invalid_image, output_path)

    def test_invalid_file_extension(self):
        # Create a sample image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)

        # Define an invalid output path
        output_path = 'test_output.txt'

        # Expect a ValueError exception
        with self.assertRaises(ValueError):
            save_image(sample_image, output_path)

if __name__ == '__main__':
    unittest.main()