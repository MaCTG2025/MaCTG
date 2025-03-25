import unittest
from apply_dynamic_color_filter import apply_dynamic_color_filter
from PIL import Image
import numpy as np

class TestDynamicColorFilter(unittest.TestCase):
    def test_apply_dynamic_color_filter(self):
        # Load a sample image
        sample_image_path = "sample_image.png"
        sample_image = Image.new("RGB", (100, 100), color=(255, 0, 0))  # Red image
        sample_image.save(sample_image_path)

        # Apply the filter with a brightness threshold
        apply_dynamic_color_filter(sample_image_path, brightness_threshold=100)

        # Load the filtered image
        filtered_image = Image.open("filtered_image.png")

        # Convert images to NumPy arrays for comparison
        sample_image_array = np.array(sample_image)
        filtered_image_array = np.array(filtered_image)

        # Check if the red pixels have been converted to grayscale
        self.assertTrue(np.all(filtered_image_array[:, :, 0] == filtered_image_array[:, :, 1] == filtered_image_array[:, :, 2]))

if __name__ == "__main__":
    unittest.main()