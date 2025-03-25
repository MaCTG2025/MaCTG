import cv2
import numpy as np
from typing import List

def process_image_with_pyramid_and_corners(
    image_path: str,
    scales: List[float],
    max_corners: int = 100,
    quality_level: float = 0.01,
    min_distance: int = 10,
    block_size: int = 3
) -> None:
    """
    Perform pyramid downscaling on the input image at specified scales, apply Shi-Tomasi corner detection
    with given parameters, and save the resulting images.

    Parameters:
    -----------
    image_path : str
        The path to the input image file (e.g., "./test_image.png").
    scales : List[float]
        A list of scaling factors for pyramid downscaling (e.g., [1.0, 0.5, 0.25]).
    max_corners : int, optional
        The maximum number of corners to detect (default is 100).
    quality_level : float, optional
        The minimal accepted quality of image corners (default is 0.01).
    min_distance : int, optional
        The minimum possible Euclidean distance between the returned corners (default is 10).
    block_size : int, optional
        The size of the neighborhood for corner detection (default is 3).

    Returns:
    --------
    None
        The function saves the resulting images to disk with filenames based on the scaling factors.
        For example, if the input image is "test_image.png", the output images will be saved as:
        - "test_image_corners_x1.png" (scale factor 1.0)
        - "test_image_corners_x0.5.png" (scale factor 0.5)
        - "test_image_corners_x0.25.png" (scale factor 0.25)

    Requirements:
    -------------
    - The input image must be a valid image file readable by OpenCV.
    - The scales must be positive floats (e.g., 1.0, 0.5, 0.25).
    - The function uses OpenCV's `cv2.pyrDown` for pyramid downscaling and `cv2.goodFeaturesToTrack`
      for Shi-Tomasi corner detection.
    - The resulting images are saved in the same directory as the input image.

    Example:
    --------
    process_image_with_pyramid_and_corners(
        image_path="./test_image.png",
        scales=[1.0, 0.5, 0.25],
        max_corners=100,
        quality_level=0.01,
        min_distance=10,
        block_size=3
    )
    """
    # Load the image
    img = cv2.imread(image_path)
    
    # Iterate over each scale factor
    for scale in scales:
        # Downscale the image using pyrDown
        scaled_img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

        # Convert the image to grayscale
        g_img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2GRAY)
        
        # Detect corners using Shi-Tomasi method
        corners = cv2.goodFeaturesToTrack(g_img, maxCorners=max_corners, qualityLevel=quality_level, minDistance=min_distance, blockSize=block_size)
        
        # Draw corners on the image
        if corners is not None:
            corners = np.int0(corners)
            for i in corners:
                x, y = i.ravel()
                cv2.circle(scaled_img, (x, y), 3, (0, 0, 255), -1)
        
        # Save the image with detected corners
        output_filename = f"{image_path.split('.')[0]}_corners_x{scale:.1f}.png"
        cv2.imwrite(output_filename, scaled_img)