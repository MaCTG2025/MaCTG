import cv2

def process_image(image_path: str) -> None:
    """
    Applies a 3x3 Gaussian blur with sigmaX=5 and performs Canny edge detection on the input image.
    The resulting image is saved as 'canny_image.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image that needs to be processed. The image should be in a format
        supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved directly to the disk as 'canny_image.png'.

    Requirements:
    -------------
    1. The input image must exist at the specified path.
    2. The function uses OpenCV's `GaussianBlur` and `Canny` functions for image processing.
    3. The Gaussian blur kernel size is fixed at 3x3 with sigmaX=5.
    4. The Canny edge detection thresholds are fixed at 100 (lower threshold) and 200 (upper threshold).
    5. The output image is saved in the current working directory as 'canny_image.png'.

    Example:
    --------
    process_image("./test_image.png")
    # This will apply Gaussian blur and Canny edge detection to 'test_image.png'
    # and save the result as 'canny_image.png'.
    """
    # Load the image from the given path
    image = cv2.imread(image_path)

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (3, 3), 5)

    # Perform Canny Edge Detection
    edges = cv2.Canny(blurred_image, 100, 200)

    # Convert the edges image to grayscale
    edges_gray = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)

    # Save the resulting image
    cv2.imwrite('canny_image.png', edges_gray)