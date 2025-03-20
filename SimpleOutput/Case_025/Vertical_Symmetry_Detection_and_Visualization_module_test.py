from Vertical_Symmetry_Detection_and_Visualization import detect_and_visualize_symmetry

def test_Vertical_Symmetry_Detection_and_Visualization(image_path: str, output_path: str) -> None:
    """
    Tests the functionality of the Vertical_Symmetry_Detection_and_Visualization module.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path where the resulting image will be saved.

    Returns:
        None
    """
    # Call the module function
    detect_and_visualize_symmetry(image_path, output_path)
    print(f"Test completed. Result saved to {output_path}")

if __name__ == '__main__':
    test_Vertical_Symmetry_Detection_and_Visualization("./4star.jpg", "./symmetry_detected.png")