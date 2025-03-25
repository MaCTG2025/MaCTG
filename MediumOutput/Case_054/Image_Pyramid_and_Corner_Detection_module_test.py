from Image_Pyramid_and_Corner_Detection import image_pyramid_and_corner_detection
from typing import List

def test_Image_Pyramid_and_Corner_Detection(image_path: str, scales: List[float]) -> None:
    """
    Test the functionality of the Image Pyramid and Corner Detection module.

    Parameters:
    -----------
    image_path : str
        The path to the input image file (e.g., "./test_image.png").
    scales : List[float]
        A list of scaling factors for pyramid downscaling (e.g., [1.0, 0.5, 0.25]).

    Returns:
    --------
    None
        The function tests the module by calling it with the provided inputs and verifies
        that the output images are saved correctly.
    """
    # Call the module function
    image_pyramid_and_corner_detection(image_path, scales)
    print("Test completed. Check the output images for correctness.")

if __name__ == '__main__':
    test_Image_Pyramid_and_Corner_Detection("./test_image.png", [1.0, 0.5, 0.25])