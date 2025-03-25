import unittest
from detect_and_classify_blobs import detect_and_classify_blobs
import cv2
import numpy as np

class TestDetectAndClassifyBlobs(unittest.TestCase):
    def test_detect_and_classify_blobs(self):
        # Prepare test data
        test_image_path = "test_image.png"
        expected_output_path = "expected_output.png"

        # Create a test image with known blobs
        test_image = np.zeros((300, 300, 3), dtype=np.uint8)
        cv2.circle(test_image, (150, 150), 50, (255, 255, 255), -1)  # Large white circle
        cv2.circle(test_image, (200, 200), 20, (255, 255, 255), -1)  # Small white circle
        cv2.imwrite(test_image_path, test_image)

        # Call the function under test
        detect_and_classify_blobs(test_image_path, circularity_threshold=0.7, inertia_threshold=0.5, convexity_threshold=0.9, output_image_path=expected_output_path)

        # Load the output image
        output_image = cv2.imread(expected_output_path)

        # Check if the output image contains two keypoints (blobs)
        keypoints = cv2.SimpleBlobDetector_create().detect(output_image)
        self.assertEqual(len(keypoints), 2)

if __name__ == '__main__':
    unittest.main()