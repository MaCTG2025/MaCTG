import unittest
from apply_morphological_gradient import apply_morphological_gradient
import cv2
import os

class TestApplyMorphologicalGradient(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.png"
        self.output_image_path = "morphological_gradient.png"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_apply_morphological_gradient(self):
        # Create a test image (white square on black background)
        test_image = cv2.imread("test_data/white_square_on_black.png", cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(self.test_image_path, test_image)

        # Call the function
        apply_morphological_gradient(self.test_image_path)

        # Read the output image
        output_image = cv2.imread(self.output_image_path, cv2.IMREAD_GRAYSCALE)

        # Check if the output image has the expected dimensions
        self.assertEqual(output_image.shape, test_image.shape)

if __name__ == "__main__":
    unittest.main()