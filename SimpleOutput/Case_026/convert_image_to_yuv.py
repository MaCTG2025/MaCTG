from PIL import Image
import numpy as np
import cv2

def convert_image_to_yuv(input_image_path: str, output_image_path: str) -> None:
    """
    Reads an input image from the specified file path, converts it from its current color space 
    to the YUV color space, and saves the resulting image to the specified output path.

    Args:
        input_image_path (str): The file path of the input image to be converted. 
                                The image can be in any color space supported by OpenCV.
        output_image_path (str): The file path where the converted YUV image will be saved.

    Returns:
        None: The function does not return any value. It saves the converted image directly 
              to the specified output path.

    Requirements:
        1. The input image must exist at the specified `input_image_path`.
        2. The output directory for `output_image_path` must exist; otherwise, the function will raise an error.
        3. The function uses OpenCV for color space conversion, so the input image will be read in BGR format by default.
        4. The output image will be saved in the YUV color space as a PNG file.

    Dependencies:
        - PIL (Pillow): For opening and saving image files.
        - numpy: For handling image data as arrays.
        - cv2 (OpenCV): For converting the image to the YUV color space.

    Example:
        convert_image_to_yuv("./test_image.png", "./yuv_image.png")
    """
    # Read the image using OpenCV
    image = cv2.imread(input_image_path)
    
    # Convert the image from BGR to YUV
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    # Save the YUV image using PIL
    cv2.imwrite(output_image_path, yuv_image)