from Image_Processing_and_Edge_Detection import image_processing_and_edge_detection

def test_Image_Processing_and_Edge_Detection(input_image_path: str, output_image_path: str, kernel_size: int = 3) -> None:
    """
    Tests the basic functionality of the Image_Processing_and_Edge_Detection module.

    Inputs:
        input_image_path (str): The file path of the input image to be processed.
        output_image_path (str): The file path where the resulting edge map will be saved.
        kernel_size (int, optional): The size of the Sobel kernel. Default is 3.

    Output:
        None: The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    image_processing_and_edge_detection(input_image_path, output_image_path, kernel_size)
    
    # Print a success message
    print(f"Test passed: Edge detection completed successfully. Result saved to {output_image_path}.")

if __name__ == '__main__':
    test_Image_Processing_and_Edge_Detection("./test_image.png", "sobel_edges.png", kernel_size=3)