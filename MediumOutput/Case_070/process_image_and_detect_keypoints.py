import cv2
import numpy as np

def process_image_and_detect_keypoints(image_path: str) -> None:
    """
    Loads an image from the specified path, splits it into R, G, and B channels, 
    applies ORB keypoint detection to each channel, draws the keypoints in red, 
    and saves the results as 'keypoints_R.png', 'keypoints_G.png', and 'keypoints_B.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves the processed images directly to disk.

    Requirements:
    -------------
    1. The input image must be a valid image file path.
    2. The function uses OpenCV's ORB (Oriented FAST and Rotated BRIEF) for keypoint detection.
    3. Keypoints are drawn in red on each channel (R, G, B) and saved as separate files.
    4. The saved images will be named 'keypoints_R.png', 'keypoints_G.png', and 'keypoints_B.png'.
    5. The function assumes the input image is in RGB format.

    Dependencies:
    -------------
    - OpenCV (cv2): For image loading, splitting channels, keypoint detection, and drawing.
    - NumPy (numpy): For handling image arrays.

    Example:
    --------
    process_image_and_detect_keypoints('./test_image.png')
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Split the image into R, G, and B channels
    b_channel, g_channel, r_channel = cv2.split(image)
    
    # Initialize ORB detector
    orb = cv2.ORB_create()
    
    # Detect keypoints and descriptors in each channel
    keypoints_r, _ = orb.detectAndCompute(r_channel, None)
    keypoints_g, _ = orb.detectAndCompute(g_channel, None)
    keypoints_b, _ = orb.detectAndCompute(b_channel, None)
    
    # Draw keypoints on each channel in red
    image_r_with_keypoints = cv2.drawKeypoints(r_channel, keypoints_r, None, color=(0, 0, 255), flags=0)
    image_g_with_keypoints = cv2.drawKeypoints(g_channel, keypoints_g, None, color=(0, 0, 255), flags=0)
    image_b_with_keypoints = cv2.drawKeypoints(b_channel, keypoints_b, None, color=(0, 0, 255), flags=0)
    
    # Save the images with keypoints
    cv2.imwrite('keypoints_R.png', image_r_with_keypoints)
    cv2.imwrite('keypoints_G.png', image_g_with_keypoints)
    cv2.imwrite('keypoints_B.png', image_b_with_keypoints)