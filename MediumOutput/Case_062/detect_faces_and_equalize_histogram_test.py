import unittest
from detect_faces_and_equalize_histogram import detect_faces_and_equalize_histogram
import cv2
import os

class TestDetectFacesAndEqualizeHistogram(unittest.TestCase):
    def setUp(self):
        self.image_path = "./test_image.png"
        self.cascade_path = "./haarcascade_frontalface_default.xml"
        self.output_path = "test_image_faces.png"

    def test_face_detection_and_histogram_equalization(self):
        # Create a mock image with a face
        mock_img = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.rectangle(mock_img, (70, 70), (130, 130), (255, 255, 255), -1)
        cv2.imwrite(self.image_path, mock_img)

        # Call the function
        detect_faces_and_equalize_histogram(self.image_path, self.cascade_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_path))

        # Read the output image
        output_img = cv2.imread(self.output_path)
        output_gray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)

        # Check if the face region has been equalized
        face_region = output_gray[70:130, 70:130]
        self.assertNotEqual(np.mean(face_region), 0)

if __name__ == "__main__":
    unittest.main()