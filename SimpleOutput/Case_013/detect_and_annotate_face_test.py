import unittest
from detect_and_annotate_face import detect_and_annotate_face
import cv2
import os

class TestDetectAndAnnotateFace(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_image.png"
        self.cascade_path = "haarcascade_frontalface_default.xml"
        self.output_image_path = "face_detected.png"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_detect_and_annotate_face_single_face(self):
        # Create a test image with a single face
        img = cv2.imread("single_face_test_image.png")
        cv2.imwrite(self.image_path, img)

        # Call the function
        detect_and_annotate_face(self.image_path, self.cascade_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the output image and check if the rectangle is drawn correctly
        output_img = cv2.imread(self.output_image_path)
        gray_output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(self.cascade_path).detectMultiScale(gray_output_img)
        self.assertEqual(len(faces), 1)
        x, y, w, h = faces[0]
        self.assertGreaterEqual(x, 0)
        self.assertGreaterEqual(y, 0)
        self.assertLessEqual(x + w, output_img.shape[1])
        self.assertLessEqual(y + h, output_img.shape[0])

    def test_detect_and_annotate_face_no_face(self):
        # Create a test image without any faces
        img = cv2.imread("no_face_test_image.png")
        cv2.imwrite(self.image_path, img)

        # Call the function
        detect_and_annotate_face(self.image_path, self.cascade_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the output image and check if no rectangle is drawn
        output_img = cv2.imread(self.output_image_path)
        gray_output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(self.cascade_path).detectMultiScale(gray_output_img)
        self.assertEqual(len(faces), 0)

if __name__ == "__main__":
    unittest.main()