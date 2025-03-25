import unittest
from apply_inverse_radon_transform import apply_inverse_radon_transform
import numpy as np
from skimage.io import imread

class TestApplyInverseRadonTransform(unittest.TestCase):
    def test_apply_inverse_radon_transform(self):
        # Create a sample Radon-transformed image
        sample_radon_transformed_image = np.array([
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ])
        
        # Define the output image path
        output_image_path = 'test_reconstructed_image.png'
        
        # Call the function with the sample input
        reconstructed_image = apply_inverse_radon_transform(sample_radon_transformed_image, output_image_path)
        
        # Load the saved reconstructed image
        loaded_reconstructed_image = imread(output_image_path)
        
        # Check if the reconstructed image is of the same shape as the input
        self.assertEqual(reconstructed_image.shape, sample_radon_transformed_image.shape)
        
        # Check if the reconstructed image is not empty
        self.assertFalse(np.all(loaded_reconstructed_image == 0))

if __name__ == '__main__':
    unittest.main()