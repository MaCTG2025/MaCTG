import unittest
from process_image_and_detect_keypoints import process_image_and_detect_keypoints
import cv2
import os

class TestProcessImageAndDetectKeypoints(unittest.TestCase):
    def setUp(self):
        self.test_image_path = './test_image.png'
        self.expected_files = ['keypoints_R.png', 'keypoints_G.png', 'keypoints_B.png']

    def test_process_image_and_detect_keypoints(self):
        # Call the function with the test image path
        process_image_and_detect_keypoints(self.test_image_path)
        
        # Check if the expected output files exist
        for file in self.expected_files:
            self.assertTrue(os.path.exists(file))
            
        # Load the saved images and check if they contain keypoints
        for i, file in enumerate(self.expected_files):
            image = cv2.imread(file)
            keypoints_count = len(cv2.goodFeaturesToTrack(image, maxCorners=None, qualityLevel=0.01, minDistance=10))
            self.assertGreater(keypoints_count, 0, f"No keypoints detected in {file}")

if __name__ == '__main__':
    unittest.main()