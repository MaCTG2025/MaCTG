import numpy as np
import cv2

def image_processing_pipeline(image_path: str, mean: float, std_dev: float, kernel_size: int, output_path: str) -> None:
    """
    Combines all the above steps into a single pipeline function for convenience.

    Args:
        image_path (str): The file path of the input image.
        mean (float): The mean of the Gaussian noise distribution.
        std_dev (float): The standard deviation of the Gaussian noise distribution.
        kernel_size (int): The size of the kernel for median filtering.
        output_path (str): The file path where the final image with detected corners will be saved.

    Returns:
        None

    Requirements:
        - The input image path must be valid and point to an existing image file.
        - The mean and standard deviation must be valid floating-point numbers.
        - The kernel size must be an odd integer greater than 1.
        - The output path must be a valid file path with a supported image format (e.g., .png, .jpg).
        - The function should handle grayscale images.
    """
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Validate kernel size
    if not isinstance(kernel_size, int) or kernel_size % 2 == 0 or kernel_size <= 1:
        raise ValueError("Kernel size must be an odd integer greater than 1.")
    
    # Add Gaussian noise
    gaussian_noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, gaussian_noise)
    
    # Apply median filtering
    filtered_image = cv2.medianBlur(noisy_image, kernel_size)
    
    # Convert to BGR for corner detection
    gray_filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_GRAY2BGR)
    
    # Detect corners using Harris corner detection
    gray = cv2.cvtColor(gray_filtered_image, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
    dst = cv2.dilate(dst, None)
    gray_filtered_image[dst > 0.01 * dst.max()] = [0, 0, 255]
    
    # Save the final image
    cv2.imwrite(output_path, gray_filtered_image)