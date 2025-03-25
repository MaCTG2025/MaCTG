import unittest
from apply_affine_transform import apply_affine_transform
import numpy as np
import cv2

class TestApplyAffineTransform(unittest.TestCase):
    def test_apply_affine_transform(self):
        # Create a sample image
        height, width, channels = 100, 100, 3
        sample_image = np.zeros((height, width, channels), dtype=np.uint8)
        sample_image[50, 50] = [255, 255, 255]  # Mark the center pixel

        # Apply the affine transform
        transformed_image = apply_affine_transform(sample_image)

        # Check if the transformed image has the same dimensions and channels
        self.assertEqual(transformed_image.shape, sample_image.shape)

        # Check if the center pixel is still visible after transformation
        center_pixel = transformed_image[50, 50]
        self.assertTrue(np.any(center_pixel != [0, 0, 0]))

if __name__ == '__main__':
    unittest.main()