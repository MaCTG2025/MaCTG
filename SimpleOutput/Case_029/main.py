from Largest_Connected_Component_Extraction import process_image_and_extract_largest_component

def main() -> None:
    """
    Entry point for the project. Processes the input image to extract the largest connected component,
    switches all other pixels to black, and saves the resulting image as 'largest_connected_component.png'.
    """
    image_path = "./shapes_r.png"
    process_image_and_extract_largest_component(image_path)

if __name__ == '__main__':
    main()