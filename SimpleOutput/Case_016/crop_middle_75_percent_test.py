import unittest
from crop_middle_75_percent import crop_middle_75_percent
from PIL import Image

class TestCropMiddle75Percent(unittest.TestCase):
    def test_crop_middle_75_percent(self):
        input_image_path = "test_image.png"
        output_image_path = "cropped_image.png"

        # Create a test image
        test_image = Image.new("RGB", (400, 300), color="red")
        test_image.save(input_image_path)

        # Call the function to crop the image
        crop_middle_75_percent(input_image_path, output_image_path)

        # Open the cropped image and check its size
        cropped_image = Image.open(output_image_path)
        self.assertEqual(cropped_image.width, 300)
        self.assertEqual(cropped_image.height, 225)

        # Close the images
        test_image.close()
        cropped_image.close()

if __name__ == "__main__":
    unittest.main()