import cv2
import numpy as np

def process_image(input_image_path: str, output_image_path: str) -> None:
    """
    Processes the input image by performing the following steps:
    1. Converts the image to grayscale.
    2. Applies Gaussian Blur to the upper half of the grayscale image.
       - The Gaussian Blur uses a kernel size of 21x21 and sigmaX=11.
    3. Saves the resulting image to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. Example: "./test_image.png".
    output_image_path : str
        The file path where the processed image will be saved. Example: "test_image_filtered.png".

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved directly to the specified output path.

    Requirements:
    -------------
    - The input image must exist at the specified path.
    - The output directory must be writable.
    - The Gaussian Blur is applied only to the upper half of the image.

    Example Usage:
    --------------
    process_image("./test_image.png", "test_image_filtered.png")
    """
    # Load the image
    image = cv2.imread(input_image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Get the dimensions of the image
    height, width = gray_image.shape
    
    # Apply Gaussian Blur to the upper half of the image
    blur_height = height // 2
    blurred_upper_half = cv2.GaussianBlur(gray_image[:blur_height], (21, 21), 11)
    
    # Combine the blurred upper half with the lower half
    result_image = np.vstack((blurred_upper_half, gray_image[blur_height:]))
    
    # Save the resulting image
    cv2.imwrite(output_image_path, result_image)