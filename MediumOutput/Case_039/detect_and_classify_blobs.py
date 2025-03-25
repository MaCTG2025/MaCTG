import cv2
import numpy as np

def detect_and_classify_blobs(
    image_path: str,
    circularity_threshold: float = 0.7,
    inertia_threshold: float = 0.5,
    convexity_threshold: float = 0.9,
    output_image_path: str = "blobs_image.png"
) -> None:
    """
    Detects blobs in the provided image using SimpleBlobDetector, classifies them based on circularity, inertia, and convexity thresholds,
    and saves the image with highlighted blobs.

    Parameters:
    -----------
    image_path : str
        The file path to the input image where blobs are to be detected.
    circularity_threshold : float, optional (default=0.7)
        The threshold for circularity to classify blobs. Blobs with circularity below this threshold will be filtered out.
    inertia_threshold : float, optional (default=0.5)
        The threshold for inertia to classify blobs. Blobs with inertia below this threshold will be filtered out.
    convexity_threshold : float, optional (default=0.9)
        The threshold for convexity to classify blobs. Blobs with convexity below this threshold will be filtered out.
    output_image_path : str, optional (default="blobs_image.png")
        The file path where the output image with highlighted blobs will be saved.

    Returns:
    --------
    None
        The function does not return any value. It saves the processed image to the specified output path.

    Requirements:
    -------------
    - The input image must be in a format supported by OpenCV (e.g., JPEG, PNG).
    - The SimpleBlobDetector parameters (circularity, inertia, and convexity thresholds) must be set appropriately to detect and classify blobs.
    - The output image will highlight the detected blobs based on the provided thresholds.

    Example:
    --------
    detect_and_classify_blobs("./blobs.jpg", circularity_threshold=0.7, inertia_threshold=0.5, convexity_threshold=0.9, output_image_path="blobs_image.png")
    """
    # Load the image
    image = cv2.imread(image_path)

    # Define the parameters for blob detection
    params = cv2.SimpleBlobDetector_Params()

    # Filter by Color.
    params.filterByColor = False

    # Filter by Area.
    params.minArea = 100
    params.maxArea = 10000

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = circularity_threshold

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = inertia_threshold

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = convexity_threshold

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(image)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Save the output image
    cv2.imwrite(output_image_path, im_with_keypoints)