import unittest
from apply_radon_transform import apply_radon_transform
from skimage.io import imread
import os
import numpy as np

class TestApplyRadonTransform(unittest.TestCase):
    def setUp(self):
        self.input_image_path = 'test_input.png'
        self.output_image_path = 'test_output.png'

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_apply_radon_transform(self):
        # Create a sample grayscale image for testing
        sample_image = np.array([[0, 0, 0],
                                [0, 255, 0],
                                [0, 0, 0]], dtype=np.uint8)
        
        # Save the sample image
        imsave(self.input_image_path, sample_image, cmap='gray')
        
        # Call the function under test
        result = apply_radon_transform(self.input_image_path, self.output_image_path)
        
        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))
        
        # Load the output image and check its shape
        output_image = imread(self.output_image_path, as_gray=True)
        self.assertEqual(output_image.shape, (3, 3))  # Corrected shape check
        
        # Clean up the sample image file
        if os.path.exists(self.input_image_path):
            os.remove(self.input_image_path)

if __name__ == '__main__':
    unittest.main()