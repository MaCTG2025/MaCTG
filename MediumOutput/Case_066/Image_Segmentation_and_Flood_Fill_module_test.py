import cv2
import numpy as np
from Image_Segmentation_and_Flood_Fill import image_segmentation_and_flood_fill

def test_image_segmentation_and_flood_fill(image_path: str, output_path: str, threshold: int = 30) -> None:
    """
    Tests the functionality of the image_segmentation_and_flood_fill module.

    Parameters:
        image_path (str): Path to the input image file.
        output_path (str): Path where the segmented image will be saved.
        threshold (int, optional): Gradient similarity threshold for flood fill. Default is 30.

    Returns:
        None
    """
    # Call the module function
    image_segmentation_and_flood_fill(image_path, output_path, threshold)

    # Verify the output file exists
    try:
        output_image = cv2.imread(output_path)
        assert output_image is not None, "Output image was not saved correctly."
        print("Test passed: Output image saved successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == '__main__':
    test_image_segmentation_and_flood_fill("./texture_seg.png", "segmented_image.png", threshold=30)