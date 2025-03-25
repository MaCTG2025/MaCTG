import cv2

def apply_filters_and_save(input_image_path: str, output_image_path: str) -> None:
    """
    Applies a median filter (kernel size = 5) and a fast mean denoising filter 
    (h = 10, templateWindowSize = 7, searchWindowSize = 21) to the input image 
    and saves the result to the specified output path.

    Parameters:
    -----------
    input_image_path : str
        The file path of the input image to be processed. The image should be in a format 
        supported by OpenCV (e.g., PNG, JPEG).

    output_image_path : str
        The file path where the processed image will be saved. The output format will 
        be determined by the file extension (e.g., '.png' for PNG format).

    Returns:
    --------
    None
        The function does not return any value. The processed image is saved directly 
        to the specified output path.

    Requirements:
    -------------
    1. The input image must exist at the specified `input_image_path`.
    2. The output directory must exist and be writable.
    3. The function uses OpenCV's `cv2.medianBlur` for the median filter and 
       `cv2.fastNlMeansDenoising` for the fast mean denoising filter.
    4. The median filter uses a kernel size of 5.
    5. The fast mean denoising filter uses the following parameters:
       - h = 10 (parameter regulating filter strength)
       - templateWindowSize = 7 (size in pixels of the template patch used for comparison)
       - searchWindowSize = 21 (size in pixels of the window used to search for similar patches)

    Example:
    --------
    apply_filters_and_save("./test_image.png", "final_image.png")
    """
    # Read the input image
    image = cv2.imread(input_image_path)

    # Apply median blur
    median_blurred = cv2.medianBlur(image, 5)

    # Apply fast mean denoising
    denoised_image = cv2.fastNlMeansDenoisingColored(median_blurred, None, 10, 10, 7, 21)

    # Save the processed image
    cv2.imwrite(output_image_path, denoised_image)