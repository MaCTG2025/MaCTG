import cv2
import numpy as np

def process_image_and_detect_edges(input_image_path: str, output_image_path: str, kernel_size: int = 3) -> None:
    """
    Processes an input image to detect edges using the Sobel operator and saves the resulting edge map as an image file.

    Steps:
    1. Load the input image from the specified path.
    2. Convert the image to grayscale.
    3. Apply the Sobel operator to detect horizontal and vertical edges using the specified kernel size.
    4. Combine the horizontal and vertical edge maps to create a final edge map.
    5. Save the resulting edge map to the specified output path.

    Inputs:
        input_image_path (str): The file path of the input image to be processed. The image must be a valid file (e.g., PNG, JPEG).
        output_image_path (str): The file path where the resulting edge map will be saved. The output format will match the input format.
        kernel_size (int, optional): The size of the Sobel kernel. Must be an odd integer (e.g., 3, 5, 7). Default is 3.

    Output:
        None: The function does not return any value. It saves the resulting edge map as an image file.

    Requirements:
        - The input image file must exist and be readable.
        - The kernel size must be an odd integer greater than or equal to 3.
        - The output directory must exist and be writable.

    Example:
        process_image_and_detect_edges("./test_image.png", "sobel_edges.png", kernel_size=3)
    """
    # Load the input image
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Sobel operator for horizontal edges
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=kernel_size)

    # Apply the Sobel operator for vertical edges
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=kernel_size)

    # Combine the horizontal and vertical edge maps
    edge_map = np.sqrt(sobelx**2 + sobely**2).astype(np.uint8)

    # Save the resulting edge map
    cv2.imwrite(output_image_path, edge_map)