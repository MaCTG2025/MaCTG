import unittest
from apply_circular_mask_and_blur import apply_circular_mask_and_blur
import numpy as np
import cv2

class TestApplyCircularMaskAndBlur(unittest.TestCase):
    def test_apply_circular_mask_and_blur(self):
        # Create a sample image
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        image[40:60, 40:60] = [255, 255, 255]  # White square in the middle
        
        # Apply the function
        result = apply_circular_mask_and_blur(image, radius=20, kernel_size=5, sigmaX=1)
        
        # Check if the central part remains unchanged
        self.assertTrue(np.array_equal(result[40:60, 40:60], [255, 255, 255]))
        
        # Check if the outer part is blurred
        self.assertFalse(np.array_equal(result[20:40, 20:40], [255, 255, 255]))
        
        # Check if the kernel size is even
        with self.assertRaises(ValueError):
            apply_circular_mask_and_blur(image, radius=20, kernel_size=4, sigmaX=1)

if __name__ == '__main__':
    unittest.main()