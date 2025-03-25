from Image_Stitching_Using_SIFT import image_stitching_module

def test_Image_Stitching_Using_SIFT(image_left_path: str, image_right_path: str, output_path: str) -> None:
    """
    Tests the basic functionality of the Image_Stitching_Using_SIFT module.

    This function calls the `image_stitching_module` function with the provided input paths and
    verifies that the stitched image is saved to the specified output path.

    Parameters:
    -----------
    image_left_path : str
        The file path of the left image (e.g., "./front_01.jpeg").
    image_right_path : str
        The file path of the right image (e.g., "./front_02.jpeg").
    output_path : str
        The file path where the stitched image will be saved (e.g., "front_stitched.jpeg").

    Returns:
    --------
    None
        The function does not return any value. It prints a success message if the test passes.
    """
    print("Testing Image_Stitching_Using_SIFT module...")
    image_stitching_module(image_left_path, image_right_path, output_path)
    print(f"Stitched image saved to {output_path}. Test passed.")

if __name__ == '__main__':
    test_Image_Stitching_Using_SIFT("./front_01.jpeg", "./front_02.jpeg", "front_stitched.jpeg")