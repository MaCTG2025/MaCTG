import unittest
from draw_and_save_contours import draw_and_save_contours
import cv2
import numpy as np

class TestDrawAndSaveContours(unittest.TestCase):
    def test_draw_and_save_contours(self):
        # Create a sample image
        image = np.zeros((500, 500, 3), dtype=np.uint8)
        
        # Define sample shapes and their contours
        rectangle_contour = np.array([[100, 100], [400, 100], [400, 400], [100, 400]], dtype=np.int32)
        square_contour = np.array([[200, 200], [300, 200], [300, 300], [200, 300]], dtype=np.int32)
        triangle_contour = np.array([[250, 50], [350, 150], [150, 150]], dtype=np.int32)
        circle_contour = cv2.circle(np.zeros((500, 500), dtype=np.uint8), (250, 250), 100, 255, -1)
        star_contour = cv2.starShapedContour(250, 250, 100, 50, 5)
        
        shapes = [
            (rectangle_contour, 'rectangle'),
            (square_contour, 'square'),
            (triangle_contour, 'triangle'),
            (circle_contour, 'circle'),
            (star_contour, 'star')
        ]
        
        # Define colors for each shape
        colors = {
            'rectangle': (0, 255, 0),
            'square': (0, 0, 255),
            'triangle': (255, 0, 0),
            'circle': (255, 255, 0),
            'star': (0, 255, 255)
        }
        
        # Define output path
        output_path = 'output_image.png'
        
        # Call the function
        draw_and_save_contours('sample_image.png', shapes, colors, 2, output_path)
        
        # Load the saved image
        saved_image = cv2.imread(output_path)
        
        # Check if the image has been modified
        self.assertNotEqual(saved_image.sum(), 0)

if __name__ == '__main__':
    unittest.main()