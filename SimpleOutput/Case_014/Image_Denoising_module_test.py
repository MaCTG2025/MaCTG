from Image_Denoising import image_denoising_module

def test_image_denoising_module(input_image_path: str, output_image_path: str) -> None:
    """
    Test the functionality of the `image_denoising_module` function.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be denoised.
    
    output_image_path : str
        The file path where the denoised image will be saved.
    """
    # Test the function with default parameters
    image_denoising_module(input_image_path, output_image_path)

    # Print a success message if the function runs without errors
    print("Test passed: The denoised image was successfully saved to", output_image_path)

if __name__ == '__main__':
    # Test the module with a sample input image and output path
    test_image_denoising_module("./test_image.png", "denoised_image.png")