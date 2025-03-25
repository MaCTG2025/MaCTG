import unittest
from watershed_segmentation import watershed_segmentation
import cv2
import os
import numpy as np

class TestWatershedSegmentation(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.output_image_path = "test_output.png"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_watershed_segmentation(self):
        # Create a test input image
        test_image = np.array([[0, 0, 0, 0],
                               [0, 255, 255, 0],
                               [0, 255, 255, 0],
                               [0, 0, 0, 0]], dtype=np.uint8)
        cv2.imwrite(self.input_image_path, test_image)

        # Call the function
        watershed_segmentation(self.input_image_path, self.output_image_path)

        # Load the segmented image
        segmented_image = cv2.imread(self.output_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Check if the segmented image has the correct dimensions
        self.assertEqual(segmented_image.shape, (4, 4, 3))

        # Clean up the test input image
        os.remove(self.input_image_path)

if __name__ == '__main__':
    unittest.main()