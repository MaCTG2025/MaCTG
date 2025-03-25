import cv2
import numpy as np

def process_image_with_pyramid_scaling_and_orb(image_path: str, nfeatures: int = 500) -> None:
    """
    Processes an image by performing 2 levels of pyramid scaling (upscaling and downscaling),
    detecting ORB keypoints on both scaled images, drawing the keypoints, and saving the resulting images.

    Args:
        image_path (str): The file path to the input image.
        nfeatures (int, optional): The number of ORB keypoints to detect. Defaults to 500.

    Returns:
        None: The function saves the resulting images as "orb_upscaled.png" and "orb_downscaled.png".

    Scope and Requirements:
        1. Load the image from the provided file path.
        2. Perform 2 levels of pyramid scaling:
           - Upscale the image by a factor of 2.
           - Downscale the image by a factor of 2.
        3. Detect ORB keypoints on both the upscaled and downscaled images using the specified number of features.
        4. Draw the detected keypoints on both scaled images using `cv2.drawKeypoints`.
        5. Save the resulting images as "orb_upscaled.png" and "orb_downscaled.png".
        6. Ensure the function handles potential errors, such as invalid file paths or unsupported image formats.

    Dependencies:
        - OpenCV (cv2): For image processing, ORB keypoint detection, and drawing keypoints.
        - NumPy (numpy): For handling image data as arrays.

    Example:
        process_image_with_pyramid_scaling_and_orb("./test_image.png", nfeatures=500)
    """
    try:
        # Load the image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Invalid image path or unsupported image format")

        # Initialize ORB detector
        orb = cv2.ORB_create(nfeatures)

        # Upscale the image
        img_upscaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        keypoints_upscaled, descriptors_upscaled = orb.detectAndCompute(img_upscaled, None)
        img_upscaled_with_keypoints = cv2.drawKeypoints(img_upscaled, keypoints_upscaled, None, color=(0, 255, 0), flags=0)

        # Downscale the image
        img_downscaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
        keypoints_downscaled, descriptors_downscaled = orb.detectAndCompute(img_downscaled, None)
        img_downscaled_with_keypoints = cv2.drawKeypoints(img_downscaled, keypoints_downscaled, None, color=(0, 255, 0), flags=0)

        # Save the results
        cv2.imwrite("orb_upscaled.png", img_upscaled_with_keypoints)
        cv2.imwrite("orb_downscaled.png", img_downscaled_with_keypoints)

    except Exception as e:
        print(f"An error occurred: {e}")