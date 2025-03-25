from Edge_Detection_and_Overlay import edge_detection_and_overlay

def test_edge_detection_and_overlay(image_path: str, output_path: str, threshold: int = 50, mask_weight: float = 0.2, image_weight: float = 0.8) -> None:
    """
    Tests the edge_detection_and_overlay function by running it with the provided parameters.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the output image file.
        threshold (int): Threshold value for creating the binary mask. Default is 50.
        mask_weight (float): Weight of the mask in the overlay. Default is 0.2.
        image_weight (float): Weight of the original image in the overlay. Default is 0.8.

    Returns:
        None
    """
    edge_detection_and_overlay(image_path, output_path, threshold, mask_weight, image_weight)
    print(f"Test completed. Output saved to {output_path}")

if __name__ == '__main__':
    test_edge_detection_and_overlay("./test_image.png", "edge_overlay.png")