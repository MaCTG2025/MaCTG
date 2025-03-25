from typing import List
from PIL import Image
import numpy as np
import cv2

def process_and_transform_image(image_path: str, output_points: List[List[int]]) -> None:
    """
    Load the input image from the given file path, crop the central 75% of the image, 
    apply a perspective transformation using the 4 corners of the cropped region as input points 
    and the specified output points, and save the transformed image as "perspective_transformed_image.png".

    Steps:
    1. Load the image from the provided `image_path`.
    2. Crop the central 75% of the image. The central region is calculated by taking 75% of the width 
       and height from the center of the image.
    3. Define the input points for the perspective transformation as the 4 corners of the cropped region.
    4. Apply the perspective transformation using the input points and the provided `output_points`.
    5. Save the transformed image as "perspective_transformed_image.png".

    Inputs:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        output_points (List[List[int]]): A list of 4 output points for the perspective transformation. 
            Each point is a list of two integers representing the x and y coordinates. 
            Example: [[10, 100], [10, 250], [300, 300], [300, 200]].

    Output:
        None: The function saves the transformed image to disk as "perspective_transformed_image.png".

    Dependencies:
        - PIL (Pillow) for image loading and saving.
        - numpy for array manipulation.
        - cv2 (OpenCV) for perspective transformation.

    Example:
        process_and_transform_image("./test_image.png", [[10, 100], [10, 250], [300, 300], [300, 200]])
    """
    # Load the image
    img = Image.open(image_path)
    img_np = np.array(img)

    # Calculate the dimensions of the cropped region
    h, w = img_np.shape[:2]
    top_left = (w // 4, h // 4)
    bottom_right = (3 * w // 4, 3 * h // 4)
    crop_width = bottom_right[0] - top_left[0]
    crop_height = bottom_right[1] - top_left[1]

    # Crop the image
    cropped_img = img.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    cropped_img_np = np.array(cropped_img)

    # Define the input points for the perspective transformation
    input_points = np.float32([[0, 0], [crop_width, 0], [crop_width, crop_height], [0, crop_height]])

    # Apply the perspective transformation
    M = cv2.getPerspectiveTransform(input_points, np.float32(output_points))
    transformed_img_np = cv2.warpPerspective(cropped_img_np, M, (img_np.shape[1], img_np.shape[0]))

    # Convert the transformed image back to PIL format
    transformed_img = Image.fromarray(transformed_img_np)

    # Save the transformed image
    transformed_img.save("perspective_transformed_image.png")