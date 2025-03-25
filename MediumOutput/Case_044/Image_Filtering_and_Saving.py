from apply_filters_and_save import apply_filters_and_save

def image_filtering_and_saving(input_image_path: str, output_image_path: str) -> None:
    """
    Applies a median filter and a fast mean denoising filter to the input image, 
    then saves the processed image to the specified output path.

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
    """
    apply_filters_and_save(input_image_path, output_image_path)