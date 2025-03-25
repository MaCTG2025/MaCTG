from Image_Processing_and_Transformation import image_processing_module

def test_Image_Processing_and_Transformation(image_path: str, output_points: list[list[int]]) -> None:
    """
    Test the functionality of the Image_Processing_and_Transformation module.

    Inputs:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        output_points (list[list[int]]): A list of 4 output points for the perspective transformation.
            Each point is a list of two integers representing the x and y coordinates.
            Example: [[10, 100], [10, 250], [300, 300], [300, 200]].

    Output:
        None: The function tests the module and prints a success message if the test passes.
    """
    # Call the module function
    image_processing_module(image_path, output_points)
    
    # Print a success message if no errors are raised
    print("Test passed: The image was processed and saved successfully.")

if __name__ == '__main__':
    # Define test inputs
    test_image_path = "./test_image.png"
    test_output_points = [[10, 100], [10, 250], [300, 300], [300, 200]]
    
    # Run the test
    test_Image_Processing_and_Transformation(test_image_path, test_output_points)