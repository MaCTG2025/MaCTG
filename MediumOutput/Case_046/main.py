from typing import List
from Image_Processing_and_Transformation import image_processing_module

def main() -> None:
    """
    Entry point for the image processing and transformation project.
    This function calls the image_processing_module to process the input image,
    crop its central 75%, apply a perspective transformation, and save the result.
    """
    image_path = "./test_image.png"
    output_points = [[10, 100], [10, 250], [300, 300], [300, 200]]
    image_processing_module(image_path, output_points)

if __name__ == '__main__':
    main()