import cv2
import numpy as np

def rescale_and_detect_contours(
    image_path: str,
    output_path_linear: str,
    output_path_cubic: str,
    contour_color: tuple = (255, 0, 0),
    contour_thickness: int = 3
) -> None:
    """
    Rescales the input image to 2x size using linear and cubic interpolation, detects contours in red on both rescaled images,
    and saves the results to the specified output paths.

    Parameters:
    -----------
    image_path : str
        The file path of the input image to be processed.
    output_path_linear : str
        The file path where the rescaled image using linear interpolation will be saved.
    output_path_cubic : str
        The file path where the rescaled image using cubic interpolation will be saved.
    contour_color : tuple, optional
        The color of the detected contours in RGB format. Default is (255, 0, 0) (red).
    contour_thickness : int, optional
        The thickness of the detected contours. Default is 3.

    Returns:
    --------
    None
        The function saves the rescaled images with detected contours to the specified output paths.

    Requirements:
    -------------
    1. The input image must be a valid image file (e.g., PNG, JPEG).
    2. The output paths must include valid file extensions (e.g., '.png').
    3. The contour color must be a tuple of three integers representing RGB values (0-255).
    4. The contour thickness must be a positive integer.

    Steps:
    ------
    1. Load the input image from the specified path.
    2. Rescale the image to 2x size using linear interpolation.
    3. Rescale the image to 2x size using cubic interpolation.
    4. Detect contours on both rescaled images.
    5. Draw the detected contours on the rescaled images using the specified color and thickness.
    6. Save the resulting images to the specified output paths.

    Dependencies:
    -------------
    - OpenCV (cv2) for image processing and contour detection.
    - NumPy (numpy) for array manipulation.

    Example:
    --------
    rescale_and_detect_contours(
        image_path="./test_image.png",
        output_path_linear="rescaled_linear.png",
        output_path_cubic="rescaled_cubic.png",
        contour_color=(255, 0, 0),
        contour_thickness=3
    )
    """
    # Load the input image
    image = cv2.imread(image_path)

    # Rescale the image using linear interpolation
    resized_linear = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Rescale the image using cubic interpolation
    resized_cubic = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Detect contours on the rescaled images
    gray = cv2.cvtColor(resized_linear, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(resized_linear, contours, -1, contour_color, contour_thickness)

    gray = cv2.cvtColor(resized_cubic, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(resized_cubic, contours, -1, contour_color, contour_thickness)

    # Save the resulting images
    cv2.imwrite(output_path_linear, resized_linear)
    cv2.imwrite(output_path_cubic, resized_cubic)