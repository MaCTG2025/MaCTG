from Face_Detection_and_Background_Blurring import face_detection_and_background_blurring

def test_Face_Detection_and_Background_Blurring(image_path: str, cascade_path: str, scaleFactor: float = 1.1, minNeighbors: int = 5, blur_kernel_size: tuple = (25, 25), output_path: str = "final_image.png") -> None:
    """
    Tests the `face_detection_and_background_blurring` function to ensure it works as expected.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        cascade_path (str): Path to the Haar cascade XML file (e.g., "./haarcascade_frontalface_default.xml").
        scaleFactor (float, optional): Parameter specifying how much the image size is reduced at each image scale. Defaults to 1.1.
        minNeighbors (int, optional): Parameter specifying how many neighbors each candidate rectangle should have to retain it. Defaults to 5.
        blur_kernel_size (tuple, optional): Size of the Gaussian blur kernel (width, height). Defaults to (25, 25).
        output_path (str, optional): Path to save the resulting image. Defaults to "final_image.png".

    Returns:
        None: The function tests the module and saves the processed image to the specified output path.
    """
    # Call the function to test
    face_detection_and_background_blurring(image_path, cascade_path, scaleFactor, minNeighbors, blur_kernel_size, output_path)
    print(f"Test completed. Output saved to {output_path}.")

if __name__ == '__main__':
    test_Face_Detection_and_Background_Blurring("./test_image.png", "./haarcascade_frontalface_default.xml")