from compute_gradient_magnitude import compute_gradient_magnitude
from create_binary_mask import create_binary_mask
from apply_color_overlay import apply_color_overlay
from save_output_image import save_output_image

def edge_detection_and_overlay(image_path: str, output_path: str, threshold: int = 50, mask_weight: float = 0.2, image_weight: float = 0.8) -> None:
    """
    Detects edges in the input image using the Sobel operator, creates a binary mask based on the gradient magnitude,
    applies a color overlay to the masked regions, and saves the final output image.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the output image file.
        threshold (int): Threshold value for creating the binary mask. Default is 50.
        mask_weight (float): Weight of the mask in the overlay. Default is 0.2.
        image_weight (float): Weight of the original image in the overlay. Default is 0.8.

    Returns:
        None
    """
    gradient_magnitude = compute_gradient_magnitude(image_path)
    binary_mask = create_binary_mask(gradient_magnitude, threshold)
    overlay_image = apply_color_overlay(image_path, binary_mask, mask_weight, image_weight)
    save_output_image(overlay_image, output_path)

if __name__ == '__main__':
    edge_detection_and_overlay('./test_image.png', 'edge_overlay.png')