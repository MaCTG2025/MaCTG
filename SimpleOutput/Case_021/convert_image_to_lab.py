import cv2  # OpenCV for image processing

def convert_image_to_lab(input_image_path: str, output_image_path: str) -> None:
    """
    Reads an input image from the specified file path, converts it to the LAB color space,
    and saves the resulting LAB image to a new file.

    Args:
        input_image_path (str): The file path of the input image to be converted.
                               Example: "./test_image.png"
        output_image_path (str): The file path where the LAB-converted image will be saved.
                                 Example: "lab_image.png"

    Returns:
        None: The function does not return any value. It saves the LAB-converted image to disk.

    Requirements:
        1. The input image must be in a format supported by OpenCV (e.g., PNG, JPEG).
        2. The function uses OpenCV's `cv2.cvtColor` method to convert the image to the LAB color space.
        3. The output image is saved in the same format as the input image unless specified otherwise.
        4. Ensure the input file path exists and is accessible; otherwise, the function will raise an error.
        5. The output directory must be writable; otherwise, the function will raise an error.

    Example Usage:
        convert_image_to_lab("./test_image.png", "lab_image.png")

    Dependencies:
        - OpenCV (cv2): Required for reading, converting, and saving images.
    """
    # Read the input image
    image = cv2.imread(input_image_path)
    
    # Convert the image to the LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    # Save the LAB-converted image to the output file path
    cv2.imwrite(output_image_path, lab_image)