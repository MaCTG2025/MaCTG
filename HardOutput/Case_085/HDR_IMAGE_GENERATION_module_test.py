from HDR_IMAGE_GENERATION import hdr_image_generation

def test_HDR_IMAGE_GENERATION() -> None:
    """
    Tests the basic functionality of the HDR_IMAGE_GENERATION module.
    """
    # Example input parameters
    image_paths = ["./hdr_1.png", "./hdr_2.png", "./hdr_3.png"]
    exposure_times = [0.5, 2.0, 16.0]
    output_path = "./hdr_image.hdr"

    # Call the function to generate the HDR image
    hdr_image_generation(image_paths, exposure_times, output_path)

    # Print a success message if no errors occur
    print("Test passed: HDR image generated and saved successfully.")

if __name__ == '__main__':
    test_HDR_IMAGE_GENERATION()