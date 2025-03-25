from calculate_energy_map import calculate_energy_map
from find_seam import find_seam
from insert_seam import insert_seam
import numpy as np

def resize_image(image: np.array, scale_factor: float) -> np.array:
    """
    Resize the input image by inserting seams based on energy functions, without distorting important content.

    Parameters:
    -----------
    image : np.array
        A 3D array representing the input image with shape (height × width × 3) for RGB channels.
    scale_factor : float
        The factor by which the width of the image should be scaled.

    Returns:
    --------
    resized_image : np.array
        A 3D array representing the resized image with shape (height × new_width × 3) for RGB channels,
        where new_width = width * scale_factor.

    Requirements:
    -------------
    - The image should be resized by iteratively calculating the energy map, finding the optimal seam,
      and inserting the seam until the desired width is achieved.
    - The resized image should maintain the original image's content without distortion.
    """
    target_width = int(image.shape[1] * scale_factor)
    resized_image = np.copy(image)

    while resized_image.shape[1] < target_width:
        energy_map = calculate_energy_map(resized_image)
        seam = find_seam(energy_map)
        resized_image = insert_seam(resized_image, seam)

    return resized_image

if __name__ == '__main__':
    # Entry point function calls
    import cv2
    input_image = cv2.imread('./test_image.png')
    resized_image = resize_image(input_image, 1.2)
    cv2.imwrite('./test_image_double_size.png', resized_image)