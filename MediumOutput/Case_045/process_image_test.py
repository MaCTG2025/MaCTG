import unittest
from process_image import process_image
from PIL import Image
import numpy as np

class TestProcessImage(unittest.TestCase):
    def test_process_image(self):
        # Create a sample image for testing
        sample_image = Image.new('RGB', (200, 200), color='white')
        sample_image.save('sample_image.png')

        # Define test parameters
        circle_radius = 50
        addition_value = 50
        subtraction_value = 100
        output_path = 'processed_image.png'

        # Call the function to be tested
        process_image('sample_image.png', circle_radius, addition_value, subtraction_value, output_path)

        # Load the processed image
        processed_image = Image.open(output_path)
        processed_image_array = np.array(processed_image)

        # Check if the central circle region has been correctly processed
        center_x, center_y = 100, 100
        radius_squared = circle_radius ** 2
        for x in range(center_x - circle_radius, center_x + circle_radius + 1):
            for y in range(center_y - circle_radius, center_y + circle_radius + 1):
                distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
                if distance_squared <= radius_squared:
                    # Check if the central circle region has been increased by addition_value
                    self.assertTrue(processed_image_array[y, x].sum() >= 50)
                else:
                    # Check if the outer region has been decreased by subtraction_value
                    self.assertTrue(processed_image_array[y, x].sum() <= 155)  # 255 - 100 = 155

if __name__ == '__main__':
    unittest.main()