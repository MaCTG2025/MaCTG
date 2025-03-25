from generate_hdr_image import generate_hdr_image

def hdr_image_generation(image_paths: list[str], exposure_times: list[float], output_path: str) -> None:
    """
    Merges a list of images taken at different exposure levels into a single HDR image and saves the output.

    Args:
        image_paths (list[str]): List of file paths to the input images.
        exposure_times (list[float]): List of exposure times corresponding to each image.
        output_path (str): File path where the HDR image will be saved.

    Returns:
        None: The function does not return any value. The HDR image is saved to the specified output path.

    Example Usage:
        hdr_image_generation(
            image_paths=["./hdr_1.png", "./hdr_2.png", "./hdr_3.png"],
            exposure_times=[0.5, 2.0, 16.0],
            output_path="./hdr_image.hdr"
        )
    """
    generate_hdr_image(image_paths, exposure_times, output_path)