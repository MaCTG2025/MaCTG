from Shape_Detection_and_Contour_Drawing import process_image_with_shapes

def test_Shape_Detection_and_Contour_Drawing(input_image_path: str, output_image_path: str) -> None:
    """
    Tests the Shape_Detection_and_Contour_Drawing module by processing an input image and saving the output image.

    Args:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the output image file.

    Returns:
        None: The function processes the image and saves the output.
    """
    # Call the module function to process the image
    process_image_with_shapes(input_image_path, output_image_path)
    print(f"Test completed. Output image saved to: {output_image_path}")

if __name__ == '__main__':
    # Define input and output paths for testing
    input_image_path = "./someshapes.jpg"
    output_image_path = "shapes_image.png"
    
    # Run the test
    test_Shape_Detection_and_Contour_Drawing(input_image_path, output_image_path)