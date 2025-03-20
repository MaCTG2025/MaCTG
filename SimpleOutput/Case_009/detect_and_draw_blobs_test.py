import unittest
from detect_and_draw_blobs import detect_and_draw_blobs
import cv2
import os

class TestDetectAndDrawBlobs(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.jpg"
        self.expected_output_path = "blobs_image.png"

    def test_detect_and_draw_blobs(self):
        # Create a test image with known blobs
        test_image = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.circle(test_image, (250, 250), 100, (255, 255, 255), -1)
        cv2.circle(test_image, (100, 100), 50, (255, 255, 255), -1)
        cv2.imwrite(self.test_image_path, test_image)

        # Call the function under test
        detect_and_draw_blobs(self.test_image_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.expected_output_path))

        # Read the output image and check if it has the expected number of keypoints
        output_image = cv2.imread(self.expected_output_path)
        keypoints = cv2.SimpleBlobDetector_create().detect(output_image)
        self.assertEqual(len(keypoints), 2)

if __name__ == '__main__':
    unittest.main()