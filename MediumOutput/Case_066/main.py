import os
import cv2
import numpy as np
from divide_image_and_apply_flood_fill import divide_image_and_apply_flood_fill
from save_segmented_image import save_segmented_image

def image_segmentation_and_flood_fill(image_path: str, output_path: str, threshold: int = 30) -> None:
    """
    Performs image segmentation by dividing the image into four regions, applying flood fill based on gradient similarity,
    and saving the segmented image to the specified output path.

    Parameters:
        image_path (str): Path to the input image file.
        output_path (str): Path where the segmented image will be saved.
        threshold (int, optional): Gradient similarity threshold for flood fill. Default is 30.

    Returns:
        None
    """
    segmented_image = divide_image_and_apply_flood_fill(image_path, threshold)
    save_segmented_image(segmented_image, output_path)

if __name__ == '__main__':
    image_segmentation_and_flood_fill('./texture_seg.png', 'segmented_image.png')