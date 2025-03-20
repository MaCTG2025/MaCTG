from Image_Pyramid_Scaling import image_pyramid_scaling_module

def test_image_pyramid_scaling_module(input_image_path: str) -> None:
    """
    Test the functionality of the `image_pyramid_scaling_module` function.

    This test function checks if the module correctly performs pyramid scaling (upscaling and downscaling)
    on an input image and returns the expected file paths for the saved images.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image that needs to be processed.
    """
    # Call the module function
    upscaled_path, downscaled_path = image_pyramid_scaling_module(input_image_path)

    # Print the results for verification
    print(f"Upscaled image saved at: {upscaled_path}")
    print(f"Downscaled image saved at: {downscaled_path}")

    # Verify the output types
    assert isinstance(upscaled_path, str), "Upscaled image path should be a string."
    assert isinstance(downscaled_path, str), "Downscaled image path should be a string."

    # Verify the output file names
    assert upscaled_path.endswith("upscaled.png"), "Upscaled image should be saved as 'upscaled.png'."
    assert downscaled_path.endswith("downscaled.png"), "Downscaled image should be saved as 'downscaled.png'."

    print("Test passed: Module functionality is working as expected.")

if __name__ == '__main__':
    test_image_pyramid_scaling_module("./test_image.png")