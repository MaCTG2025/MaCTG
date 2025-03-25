import unittest
from apply_filters_and_save import apply_filters_and_save
import cv2
import os

class TestApplyFiltersAndSave(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "./test_image.png"
        self.output_image_path = "./processed_image.png"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_apply_filters_and_save(self):
        # Ensure the input image exists
        self.assertTrue(os.path.exists(self.input_image_path))

        # Call the function
        apply_filters_and_save(self.input_image_path, self.output_image_path)

        # Check if the output image was created
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the images to check if they have been processed
        input_image = cv2.imread(self.input_image_path)
        output_image = cv2.imread(self.output_image_path)

        # Check if the dimensions match
        self.assertEqual(input_image.shape, output_image.shape)

        # Check if the images are different (i.e., filters were applied)
        self.assertFalse((input_image == output_image).all())

if __name__ == "__main__":
    unittest.main()