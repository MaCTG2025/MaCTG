import unittest
from multi_scale_template_matching import multi_scale_template_matching
import cv2
import os
import numpy as np

class TestMultiScaleTemplateMatching(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_image.jpg"
        self.template_path = "test_template.jpg"
        self.output_path = "output_image.jpg"
        self.scales = [0.5, 0.75, 1.25, 1.5]

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_multi_scale_template_matching(self):
        # Create test images
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.circle(img, (250, 250), 50, (255, 255, 255), -1)
        cv2.imwrite(self.image_path, img)

        template = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.circle(template, (50, 50), 25, (255, 255, 255), -1)
        cv2.imwrite(self.template_path, template)

        # Call the function
        multi_scale_template_matching(self.image_path, self.template_path, self.scales, self.output_path)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_path))

        # Read the output image
        output_img = cv2.imread(self.output_path)

        # Check if the bounding box is drawn correctly
        contours, _ = cv2.findContours(cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.assertEqual(len(contours), 1)
        contour = contours[0]
        x, y, w, h = cv2.boundingRect(contour)
        self.assertAlmostEqual(x, 200, delta=10)
        self.assertAlmostEqual(y, 200, delta=10)
        self.assertAlmostEqual(w, 100, delta=10)
        self.assertAlmostEqual(h, 100, delta=10)

if __name__ == '__main__':
    unittest.main()