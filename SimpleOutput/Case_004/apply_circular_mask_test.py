import unittest
from apply_circular_mask import apply_circular_mask
from PIL import Image

class TestApplyCircularMask(unittest.TestCase):
    def test_apply_circular_mask(self):
        input_image_path = "test_image.png"
        output_image_path = "masked_image.png"
        mask_radius = 100
        
        # Create a test image
        test_img = Image.new('RGBA', (200, 200), color=(255, 0, 0))
        test_img.save(input_image_path)
        
        # Apply the circular mask
        apply_circular_mask(input_image_path, output_image_path, mask_radius)
        
        # Load the output image
        output_img = Image.open(output_image_path)
        
        # Check if the image has the correct size
        self.assertEqual(output_img.size, (200, 200))
        
        # Check if the pixels outside the mask are black
        for x in range(200):
            for y in range(200):
                if (x - 100)**2 + (y - 100)**2 > 100**2:
                    self.assertEqual(output_img.getpixel((x, y)), (0, 0, 0, 0))
        
        # Check if the pixels inside the mask are white
        for x in range(200):
            for y in range(200):
                if (x - 100)**2 + (y - 100)**2 <= 100**2:
                    self.assertEqual(output_img.getpixel((x, y)), (255, 0, 0, 255))

if __name__ == '__main__':
    unittest.main()