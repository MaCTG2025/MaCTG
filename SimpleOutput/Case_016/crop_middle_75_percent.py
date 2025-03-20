from PIL import Image

def crop_middle_75_percent(input_image_path: str, output_image_path: str) -> None:
    """
    Crop the middle 75% of the input image and save the result to the specified output path.

    The function reads an image from the given input path, calculates the middle 75% of the image
    (both width and height), crops the image to this region, and saves the cropped image to the
    specified output path.

    Args:
        input_image_path (str): The file path of the input image to be cropped. The image should
            be in a format supported by the PIL library (e.g., PNG, JPEG).
        output_image_path (str): The file path where the cropped image will be saved. The output
            format will be determined by the file extension provided in this path.

    Returns:
        None: The function does not return any value. It saves the cropped image directly to the
            specified output path.

    Raises:
        FileNotFoundError: If the input image file does not exist at the provided `input_image_path`.
        IOError: If the output directory is not writable or the output file cannot be saved.

    Requirements:
        - The input image must exist at the provided `input_image_path`.
        - The output directory must exist or be writable; otherwise, an error will occur.
        - The function uses the Python Imaging Library (PIL) via the `Pillow` package for image processing.

    Example:
        crop_middle_75_percent("./test_image.png", "./cropped_image.png")
    """
    # Open the input image
    with Image.open(input_image_path) as img:
        # Calculate the dimensions for cropping
        width, height = img.size
        new_width = int(width * 0.75)
        new_height = int(height * 0.75)
        
        # Calculate the left and upper coordinates for cropping
        left = (width - new_width) // 2
        top = (height - new_height) // 2
        
        # Crop the image
        cropped_img = img.crop((left, top, left + new_width, top + new_height))
        
        # Save the cropped image to the output path
        cropped_img.save(output_image_path)