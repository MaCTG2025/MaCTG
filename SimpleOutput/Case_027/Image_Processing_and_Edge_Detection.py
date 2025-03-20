from process_image_and_detect_edges import process_image_and_detect_edges

def image_processing_and_edge_detection(input_image_path: str, output_image_path: str, kernel_size: int = 3) -> None:
    """
    Processes an input image to detect edges using the Sobel operator and saves the resulting edge map as an image file.

    This module-level function encapsulates the edge detection process by calling the `process_image_and_detect_edges` function.

    Inputs:
        input_image_path (str): The file path of the input image to be processed. The image must be a valid file (e.g., PNG, JPEG).
        output_image_path (str): The file path where the resulting edge map will be saved. The output format will match the input format.
        kernel_size (int, optional): The size of the Sobel kernel. Must be an odd integer (e.g., 3, 5, 7). Default is 3.

    Output:
        None: The function does not return any value. It saves the resulting edge map as an image file.

    Example:
        image_processing_and_edge_detection("./test_image.png", "sobel_edges.png", kernel_size=3)
    """
    process_image_and_detect_edges(input_image_path, output_image_path, kernel_size)