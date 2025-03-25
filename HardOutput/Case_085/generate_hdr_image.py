import cv2
import numpy as np

def generate_hdr_image(image_paths: list[str], exposure_times: list[float], output_path: str) -> None:
    """
    Merges a list of images taken at different exposure levels into a single HDR image and saves the output.

    Args:
        image_paths (list[str]): A list of file paths to the input images. Each image should be in a format 
                                 supported by OpenCV (e.g., PNG, JPEG). Example: ["./hdr_1.png", "./hdr_2.png", "./hdr_3.png"].
        exposure_times (list[float]): A list of exposure times corresponding to each image. The exposure times 
                                      should be in seconds. Example: [0.5, 2.0, 16.0].
        output_path (str): The file path where the resulting HDR image will be saved. The output file should 
                           have the '.hdr' extension. Example: "./hdr_image.hdr".

    Returns:
        None: The function does not return any value. The HDR image is saved to the specified output path.

    Requirements:
        1. The number of image paths must match the number of exposure times.
        2. The images must be aligned (e.g., taken from the same camera position).
        3. The exposure times should be provided in seconds and correspond to the exposure levels of the images.
        4. The output path must have the '.hdr' extension to ensure the correct file format.

    Dependencies:
        - OpenCV (cv2): Used for reading images, merging them into an HDR image, and saving the output.
        - NumPy (numpy): Used for numerical operations during the HDR merging process.

    Example Usage:
        generate_hdr_image(
            image_paths=["./hdr_1.png", "./hdr_2.png", "./hdr_3.png"],
            exposure_times=[0.5, 2.0, 16.0],
            output_path="./hdr_image.hdr"
        )
    """
    # Read images
    images = [cv2.imread(path) for path in image_paths]
    
    # convert exposure times to numpy array
    exposure_times = np.array(exposure_times, dtype=np.float32)

    # compute Camera Response Function (CRF)
    calibrate_debevec = cv2.createCalibrateDebevec()
    response_debevec = calibrate_debevec.process(images, exposure_times)
    
    # Merge images into HDR image
    merge_debevec = cv2.createMergeDebevec()
    hdr_image = merge_debevec.process(images, exposure_times, response_debevec)

    # Save LDR image
    cv2.imwrite(output_path, hdr_image)