import unittest
from add_gaussian_noise import add_gaussian_noise
import numpy as np

class TestAddGaussianNoise(unittest.TestCase):
    def test_add_gaussian_noise(self):
        # Create a sample grayscale image
        image = np.array([[100, 150], [200, 250]], dtype=np.uint8)
        
        # Define the mean and standard deviation for Gaussian noise
        mean = 0
        std_dev = 10
        
        # Call the function with the sample image and noise parameters
        noisy_image = add_gaussian_noise(image, mean, std_dev)
        
        # Check if the output image has the same shape as the input image
        self.assertEqual(noisy_image.shape, image.shape)
        
        # Check if the data type of the output image matches the input image
        self.assertEqual(noisy_image.dtype, image.dtype)
        
        # Check if the noise has been added correctly
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                self.assertTrue(abs(noisy_image[i, j] - image[i, j]) <= std_dev * 3)

if __name__ == '__main__':
    unittest.main()