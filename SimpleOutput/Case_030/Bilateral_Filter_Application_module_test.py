from Bilateral_Filter_Application import apply_bilateral_filter_module

def test_Bilateral_Filter_Application(input_image_path: str, output_image_path: str, d: int = 9, sigmaColor: float = 75.0, sigmaSpace: float = 75.0) -> None:
    """
    Tests the functionality of the Bilateral_Filter_Application module.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed.
    output_image_path : str
        The file path where the filtered image will be saved.
    d : int, optional (default=9)
        Diameter of each pixel neighborhood used during filtering.
    sigmaColor : float, optional (default=75.0)
        Filter sigma in the color space.
    sigmaSpace : float, optional (default=75.0)
        Filter sigma in the coordinate space.

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    # Call the module function
    apply_bilateral_filter_module(input_image_path, output_image_path, d, sigmaColor, sigmaSpace)
    print(f"Bilateral filter applied successfully. Output saved to {output_image_path}")

if __name__ == '__main__':
    # Test the module with default parameters
    test_Bilateral_Filter_Application("./test_image.png", "./bilateral_filtered_image.png")