import unittest
from stitch_images_using_sift import stitch_images_using_sift
import cv2
import os

class TestStitchImagesUsingSIFT(unittest.TestCase):

    def setUp(self):
        self.image_left_path = "test_front_01.jpg"
        self.image_right_path = "test_front_02.jpg"
        self.output_path = "stitched_test_image.jpg"

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_stitch_images_using_sift(self):
        # Load test images
        img_left = cv2.imread(self.image_left_path)
        img_right = cv2.imread(self.image_right_path)

        # Call the function
        stitch_images_using_sift(self.image_left_path, self.image_right_path, self.output_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_path))

        # Load the stitched image
        img_stitched = cv2.imread(self.output_path)

        # Check if the dimensions of the stitched image are correct
        expected_height = max(img_left.shape[0], img_right.shape[0])
        expected_width = img_left.shape[1] + img_right.shape[1]
        self.assertEqual(img_stitched.shape[:2], (expected_height, expected_width))

if __name__ == '__main__':
    unittest.main()