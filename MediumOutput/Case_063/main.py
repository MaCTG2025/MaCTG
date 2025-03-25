import cv2
from add_gaussian_noise import add_gaussian_noise
from apply_median_filter import apply_median_filter
from detect_corners_and_save import detect_corners_and_save

def image_processing_pipeline(image_path: str, mean: float, std_dev: float, kernel_size: int, output_path: str) -> None:
    """
    Combines all image processing steps into a single pipeline function for convenience.

    Args:
        image_path (str): The file path of the input image.
        mean (float): The mean of the Gaussian noise distribution.
        std_dev (float): The standard deviation of the Gaussian noise distribution.
        kernel_size (int): The size of the kernel for median filtering.
        output_path (str): The file path where the final image with detected corners will be saved.

    Returns:
        None

    Steps:
        1. Reads the input image.
        2. Adds Gaussian noise to the image.
        3. Applies median filtering to the noisy image.
        4. Detects corners using Harris corner detection.
        5. Saves the final image with detected corners.
    """
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Add Gaussian noise
    noisy_image = add_gaussian_noise(image, mean, std_dev)
    
    # Apply median filtering
    filtered_image = apply_median_filter(noisy_image, kernel_size)
    
    # Detect corners and save the result
    detect_corners_and_save(filtered_image, output_path)

if __name__ == '__main__':
    image_processing_pipeline('./test_image.png', 0, 25, 5, 'test_image_corners.png')