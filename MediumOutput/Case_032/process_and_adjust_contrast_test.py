import unittest
from process_and_adjust_contrast import process_and_adjust_contrast
import cv2
import numpy as np

class TestProcessAndAdjustContrast(unittest.TestCase):

    def setUp(self):
        self.test_image_path = 'test_image.jpg'
        self.output_path = 'processed_test_image.jpg'
        self.mask_length = 50
        self.mask_value = 255
        self.alpha = 1.5
        self.beta = 30

        # Create a test image
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(self.image, (25, 25), (75, 75), (255, 255, 255), -1)

        # Save the test image
        cv2.imwrite(self.test_image_path, self.image)

    def test_process_and_adjust_contrast_valid_input(self):
        process_and_adjust_contrast(self.test_image_path, self.mask_length, self.mask_value, self.alpha, self.beta, self.output_path)
        result_image = cv2.imread(self.output_path)
        self.assertIsNotNone(result_image)
        self.assertEqual(result_image.shape, (100, 100, 3))

    def test_process_and_adjust_contrast_invalid_image_path(self):
        with self.assertRaises(ValueError):
            process_and_adjust_contrast('nonexistent_image.jpg', self.mask_length, self.mask_value, self.alpha, self.beta, self.output_path)

    def test_process_and_adjust_contrast_mask_length_out_of_bounds(self):
        with self.assertRaises(ValueError):
            process_and_adjust_contrast(self.test_image_path, 150, self.mask_value, self.alpha, self.beta, self.output_path)

    def test_process_and_adjust_contrast_mask_value_out_of_range(self):
        with self.assertRaises(ValueError):
            process_and_adjust_contrast(self.test_image_path, self.mask_length, 256, self.alpha, self.beta, self.output_path)

if __name__ == '__main__':
    unittest.main()