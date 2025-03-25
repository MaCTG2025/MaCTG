from load_image import load_image
from convert_to_grayscale import convert_to_grayscale
from apply_adaptive_thresholding import apply_adaptive_thresholding
from detect_and_draw_contours import detect_and_draw_contours
from save_image import save_image

def process_image(image_path: str, output_path: str) -> None:
    """
    Process an image by converting it to grayscale, applying adaptive thresholding, detecting contours,
    and saving the final output image.

    Args:
        image_path (str): The file path of the input image.
        output_path (str): The file path where the processed image will be saved.

    Returns:
        None
    """
    image = load_image(image_path)
    gray_image = convert_to_grayscale(image)
    binary_image = apply_adaptive_thresholding(gray_image, blockSize=71, C=2)
    output_image = detect_and_draw_contours(binary_image, color=(0, 0, 255), thickness=2)
    save_image(output_image, output_path)

if __name__ == '__main__':
    process_image('./test_image.png', 'adaptive_threshold_contours.png')