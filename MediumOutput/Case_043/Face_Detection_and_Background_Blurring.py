from process_image import process_image

def face_detection_and_background_blurring(image_path: str, cascade_path: str, scaleFactor: float = 1.1, minNeighbors: int = 5, blur_kernel_size: tuple = (25, 25), output_path: str = "final_image.png") -> None:
    """
    Detects faces in the input image using Haar cascades, applies Gaussian blur to the background, and saves the resulting image.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        cascade_path (str): Path to the Haar cascade XML file (e.g., "./haarcascade_frontalface_default.xml").
        scaleFactor (float, optional): Parameter specifying how much the image size is reduced at each image scale. Defaults to 1.1.
        minNeighbors (int, optional): Parameter specifying how many neighbors each candidate rectangle should have to retain it. Defaults to 5.
        blur_kernel_size (tuple, optional): Size of the Gaussian blur kernel (width, height). Defaults to (25, 25).
        output_path (str, optional): Path to save the resulting image. Defaults to "final_image.png".

    Returns:
        None: The function saves the processed image to the specified output path.

    Steps:
        1. Calls the `process_image` function to detect faces, blur the background, and save the resulting image.
    """
    process_image(image_path, cascade_path, scaleFactor, minNeighbors, blur_kernel_size, output_path)