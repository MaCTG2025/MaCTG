import unittest
from detect_shapes_and_compute_metrics import detect_shapes_and_compute_metrics
import cv2
import numpy as np

class TestDetectShapesAndComputeMetrics(unittest.TestCase):

    def test_detect_shapes_and_compute_metrics(self):
        # Create a sample image with known shapes
        image = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(image, (10, 10), (40, 40), 255, -1)  # Square
        cv2.circle(image, (60, 60), 20, 255, -1)          # Circle
        
        # Save the sample image to a temporary file
        temp_image_path = "temp_shapes.png"
        cv2.imwrite(temp_image_path, image)
        
        # Call the function under test
        detect_shapes_and_compute_metrics(temp_image_path)
        
        # Load the saved results
        results = np.load("areas_perimeters.npy", allow_pickle=True).item()
        
        # Check if the number of shapes is correct
        self.assertEqual(len(results["areas"]), 2)
        self.assertEqual(len(results["perimeters"]), 2)
        
        # Check if the areas are approximately correct
        self.assertAlmostEqual(results["areas"][0], 900, delta=10)  # Area of square
        self.assertAlmostEqual(results["areas"][1], 1256.63706144, delta=10)  # Area of circle
        
        # Clean up the temporary image file
        import os
        os.remove(temp_image_path)
        os.remove("areas_perimeters.npy")

if __name__ == "__main__":
    unittest.main()