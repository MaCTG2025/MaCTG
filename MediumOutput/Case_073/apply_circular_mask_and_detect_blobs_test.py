import unittest
from apply_circular_mask_and_detect_blobs import apply_circular_mask_and_detect_blobs
import cv2
import os

class TestApplyCircularMaskAndDetectBlobs(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_image.jpg"
        self.output_path = "output_image.jpg"
        self.radius = 100
        
        # Create a test image
        self.test_image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.circle(self.test_image, (100, 100), 50, (255, 255, 255), -1)
        
        # Save the test image
        cv2.imwrite(self.image_path, self.test_image)

    def test_apply_circular_mask_and_detect_blobs(self):
        # Call the function
        apply_circular_mask_and_detect_blobs(self.image_path, self.radius, self.output_path)
        
        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_path))
        
        # Load the output image
        output_image = cv2.imread(self.output_path)
        
        # Check if the output image has the expected dimensions
        self.assertEqual(output_image.shape, (200, 200, 3))
        
        # Check if there are keypoints detected
        keypoints = cv2.SimpleBlobDetector_create().detect(cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY))
        self.assertGreater(len(keypoints), 0)

if __name__ == '__main__':
    unittest.main()