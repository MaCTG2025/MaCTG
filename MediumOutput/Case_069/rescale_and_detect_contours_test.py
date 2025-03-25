import unittest
from rescale_and_detect_contours import rescale_and_detect_contours
import cv2
import os

class TestRescaleAndDetectContours(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.png"
        self.output_path_linear = "rescaled_linear_test.png"
        self.output_path_cubic = "rescaled_cubic_test.png"

    def tearDown(self):
        if os.path.exists(self.output_path_linear):
            os.remove(self.output_path_linear)
        if os.path.exists(self.output_path_cubic):
            os.remove(self.output_path_cubic)

    def test_rescale_and_detect_contours(self):
        # Create a test image with some contours
        test_image = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(test_image, (10, 10), (90, 90), 255, -1)
        cv2.circle(test_image, (50, 50), 30, 255, -1)
        cv2.imwrite(self.test_image_path, test_image)

        # Call the function
        rescale_and_detect_contours(
            self.test_image_path,
            self.output_path_linear,
            self.output_path_cubic,
            contour_color=(0, 255, 0),
            contour_thickness=2
        )

        # Check if the output files exist
        self.assertTrue(os.path.exists(self.output_path_linear))
        self.assertTrue(os.path.exists(self.output_path_cubic))

        # Read the output images
        output_linear = cv2.imread(self.output_path_linear)
        output_cubic = cv2.imread(self.output_path_cubic)

        # Check if the contours are drawn correctly
        self.assertGreater(np.sum(output_linear[:, :, 1]), 0)  # Green channel should have non-zero sum
        self.assertGreater(np.sum(output_cubic[:, :, 1]), 0)   # Green channel should have non-zero sum

if __name__ == '__main__':
    unittest.main()