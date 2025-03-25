from stitch_images_using_sift import stitch_images_using_sift

def image_stitching_module(image_left_path: str, image_right_path: str, output_path: str) -> None:
    """
    Stitches two images together using the SIFT algorithm and saves the result.

    This module-level function takes the file paths of two images (left and right) and uses the
    `stitch_images_using_sift` function to stitch them together. The stitched image is saved to
    the specified output path. The function includes validation for sufficient keypoint matches
    and robust outlier filtering to ensure successful stitching.

    Parameters:
    -----------
    image_left_path : str
        The file path of the left image (e.g., "./front_01.jpeg").
    image_right_path : str
        The file path of the right image (e.g., "./front_02.jpeg").
    output_path : str
        The file path where the stitched image will be saved (e.g., "front_stitched.jpeg").

    Returns:
    --------
    None
        The function does not return any value. It saves the stitched image to the specified output path.

    Raises:
    -------
    ValueError
        If the number of matched keypoints is insufficient to compute the homography matrix.

    Example:
    --------
    image_stitching_module("./front_01.jpeg", "./front_02.jpeg", "front_stitched.jpeg")
    """
    stitch_images_using_sift(image_left_path, image_right_path, output_path)

if __name__ == '__main__':
    image_stitching_module("./front_01.jpeg", "./front_02.jpeg", "front_stitched.jpeg")