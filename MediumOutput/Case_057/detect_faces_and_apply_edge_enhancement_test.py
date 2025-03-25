import unittest
from detect_faces_and_apply_edge_enhancement import detect_faces_and_apply_edge_enhancement
import cv2
import numpy as np
import os

class TestDetectFacesAndApplyEdgeEnhancement(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_image.png"
        self.cascade_path = "haarcascade_frontalface_default.xml"
        self.output_path = "test_image_faces.png"

    def test_detect_faces_and_apply_edge_enhancement(self):
        # Create a sample image with a face
        image = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.rectangle(image, (70, 70), (130, 130), (255, 255, 255), -1)
        cv2.imwrite(self.image_path, image)

        # Call the function
        detect_faces_and_apply_edge_enhancement(self.image_path, self.cascade_path, self.output_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_path))

        # Read the output image
        output_image = cv2.imread(self.output_path)

        # Check if the face region is sharpened
        face_region = output_image[70:130, 70:130]
        mean_intensity = np.mean(face_region)
        self.assertGreater(mean_intensity, 128)

if __name__ == "__main__":
    unittest.main()