from Largest_Connected_Component_Extraction import process_image_and_extract_largest_component

def test_Largest_Connected_Component_Extraction(image_path: str) -> None:
    """
    Tests the functionality of the Largest_Connected_Component_Extraction module.
    Ensures that the module processes the input image, extracts the largest connected component,
    and saves the resulting image as 'largest_connected_component.png'.

    Parameters:
    -----------
    image_path : str
        The file path to the input image. The image should be in a format supported by OpenCV (e.g., PNG, JPEG).
    """
    # Call the module function to process the image
    process_image_and_extract_largest_component(image_path)

    # Verify that the output file was created
    import os
    if os.path.exists("largest_connected_component.png"):
        print("Test passed: Output file 'largest_connected_component.png' was created successfully.")
    else:
        print("Test failed: Output file 'largest_connected_component.png' was not created.")

if __name__ == '__main__':
    test_Largest_Connected_Component_Extraction("./shapes_r.png")