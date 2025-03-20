import cv2
import numpy as np

def apply_kernel_filter(input_image_path: str) -> None:
    """
    Applies a 3x3 kernel filter to the input image and saves the result as "filtered_image.png".

    The kernel filter is a 3x3 matrix with all elements equal to 1/9, which is a simple averaging filter.
    This filter is applied to the input image using convolution, resulting in a blurred version of the image.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./test_image.png"). The image should be in a format
        supported by OpenCV (e.g., PNG, JPEG).

    Returns:
    --------
    None
        The function does not return any value. The filtered image is saved as "filtered_image.png"
        in the current working directory.

    Requirements:
    -------------
    1. The input image must exist at the specified path.
    2. The input image must be a valid image file supported by OpenCV.
    3. The function uses OpenCV for image processing and NumPy for matrix operations.

    Example:
    --------
    apply_kernel_filter("./test_image.png")
    # This will apply the 3x3 kernel filter to "test_image.png" and save the result as "filtered_image.png".
    """
    # Read the input image
    image = cv2.imread(input_image_path)
    
    # Define the 3x3 averaging kernel
    kernel = np.ones((3, 3), np.float32) / 9
    
    # Apply the kernel filter using convolution
    filtered_image = cv2.filter2D(image, -1, kernel)
    
    # Save the filtered image
    cv2.imwrite("filtered_image.png", filtered_image)