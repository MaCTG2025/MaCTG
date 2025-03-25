import unittest
from apply_pencil_sketch_effect import apply_pencil_sketch_effect
import os
import cv2
import numpy as np

class TestApplyPencilSketchEffect(unittest.TestCase):
    def test_apply_pencil_sketch_effect(self):
        input_image_path = "test_image.png"
        output_image_path = "output_image.png"

        # Create a sample input image
        sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(input_image_path, sample_image)

        # Call the function
        apply_pencil_sketch_effect(input_image_path, output_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(output_image_path))

if __name__ == "__main__":
    unittest.main()