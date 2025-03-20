import cv2
import numpy as np

def extract_and_save_rgb_channels(image_path: str) -> None:
    """
    Splits an RGB image into its R, G, and B channels, creates three new RGB images where only one channel is non-zero,
    and saves them as 'red_channel.png', 'green_channel.png', and 'blue_channel.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input RGB image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. It saves three images to disk:
        - 'red_channel.png': An RGB image where only the red channel is non-zero.
        - 'green_channel.png': An RGB image where only the green channel is non-zero.
        - 'blue_channel.png': An RGB image where only the blue channel is non-zero.

    Requirements:
    -------------
    1. The input image must be a valid RGB image with three channels (R, G, B).
    2. The function uses OpenCV (cv2) to read and write images, so the input image format must be supported by OpenCV.
    3. The output images will be saved in the same directory as the input image unless a full path is provided.

    Example:
    --------
    Given an image at './test_image.png', the function will:
    1. Split the image into R, G, and B channels.
    2. Create three new images:
       - 'red_channel.png': Only the red channel is non-zero.
       - 'green_channel.png': Only the green channel is non-zero.
       - 'blue_channel.png': Only the blue channel is non-zero.
    3. Save the three images to disk.

    Dependencies:
    -------------
    - OpenCV (cv2): For reading and writing images.
    - NumPy (numpy): For array manipulation and channel extraction.
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Check if the image has three channels
    if image.shape[2] != 3:
        raise ValueError("The input image must have exactly three channels (RGB).")
    
    # Extract the R, G, and B channels
    b_channel = image[:, :, 0]
    g_channel = image[:, :, 1]
    r_channel = image[:, :, 2]
    
    # Create new images with only one channel non-zero
    blue_channel_img = cv2.merge((b_channel, np.zeros_like(g_channel), np.zeros_like(r_channel)))
    green_channel_img = cv2.merge((np.zeros_like(r_channel), g_channel, np.zeros_like(b_channel)))
    red_channel_img = cv2.merge((np.zeros_like(b_channel), np.zeros_like(g_channel), r_channel))
    
    # Save the new images
    cv2.imwrite('red_channel.png', red_channel_img)
    cv2.imwrite('green_channel.png', green_channel_img)
    cv2.imwrite('blue_channel.png', blue_channel_img)