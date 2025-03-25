from Image_Color_Reduction import process_image_color_reduction
import numpy as np
from PIL import Image

def test_Image_Color_Reduction(image_path: str, color_levels: list, output_path: str) -> None:
    """
    Tests the Image Color Reduction module by processing an image and saving the result.

    Args:
        image_path (str): The file path of the input image.
        color_levels (list): A list of four integers specifying the number of color levels to apply to each region.
        output_path (str): The file path where the final image will be saved.
    """
    # Call the module function
    process_image_color_reduction(image_path, color_levels, output_path)
    
    # Verify the output image exists
    try:
        output_image = Image.open(output_path)
        print(f"Output image saved successfully at {output_path}.")
        output_image.close()
    except Exception as e:
        print(f"Error: Output image could not be loaded. {e}")

if __name__ == '__main__':
    # Test parameters
    test_image_path = "./test_image.png"
    test_color_levels = [2, 4, 8, 16]
    test_output_path = "color_reduction.png"
    
    # Run the test
    test_Image_Color_Reduction(test_image_path, test_color_levels, test_output_path)