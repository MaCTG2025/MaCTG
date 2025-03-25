from process_and_adjust_contrast import process_and_adjust_contrast

def image_processing_and_contrast_adjustment(
    image_path: str,
    mask_length: int,
    mask_value: int,
    alpha: float,
    beta: int,
    output_path: str
) -> None:
    """
    Processes an RGB image by masking the center of each channel with a square of given length and value,
    applies contrast adjustment using the provided alpha and beta values, and saves the resulting image.

    Args:
        image_path (str): The file path to the input RGB image.
        mask_length (int): The length of the square mask to be applied at the center of each channel.
        mask_value (int): The value to set for the pixels within the masked area (e.g., 1 for white).
        alpha (float): The contrast adjustment factor (gain). A value of 1.0 means no change.
        beta (int): The brightness adjustment factor (bias). A value of 0 means no change.
        output_path (str): The file path where the resulting image will be saved.

    Returns:
        None: The function does not return any value. The processed image is saved to the specified output path.
    """
    process_and_adjust_contrast(image_path, mask_length, mask_value, alpha, beta, output_path)

if __name__ == '__main__':
    image_processing_and_contrast_adjustment(
        image_path='./test_image.png',
        mask_length=100,
        mask_value=1,
        alpha=1.5,
        beta=50,
        output_path='contrast_adjusted_image.png'
    )