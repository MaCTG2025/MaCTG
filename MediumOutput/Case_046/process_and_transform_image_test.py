import unittest
from process_and_transform_image import process_and_transform_image
from PIL import Image
import numpy as np
import cv2

class TestProcessAndTransformImage(unittest.TestCase):
    def test_process_and_transform_image(self):
        # Create a sample image for testing
        sample_image = Image.new('RGB', (400, 400), color='white')
        sample_image.save('sample_image.png')

        # Define the output points for the perspective transformation
        output_points = [[10, 100], [10, 250], [300, 300], [300, 200]]

        # Call the function with the sample image and output points
        process_and_transform_image('sample_image.png', output_points)

        # Load the transformed image
        transformed_image = Image.open('perspective_transformed_image.png')

        # Check if the transformed image has the correct size
        self.assertEqual(transformed_image.size, (400, 400))

        # Clean up the sample image and transformed image files
        sample_image.close()
        transformed_image.close()

if __name__ == '__main__':
    unittest.main()