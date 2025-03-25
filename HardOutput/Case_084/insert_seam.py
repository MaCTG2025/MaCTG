import numpy as np

def insert_seam(image: np.array, seam: list) -> np.array:
    """
    Insert the identified seam into the image, effectively increasing its width by 1 pixel.

    Parameters:
    -----------
    image : np.array
        A 3D array representing the input image with shape (height × width × 3) for RGB channels.
    seam : list
        A list of column indices representing the seam to be inserted.

    Returns:
    --------
    resized_image : np.array
        A 3D array representing the resized image with shape (height × new_width × 3) for RGB channels,
        where new_width = width + 1.

    Requirements:
    -------------
    - The seam should be inserted by duplicating the pixel values along the seam path.
    - The resized image should maintain the original image's content without distortion.
    """
    height, width, _ = image.shape
    new_width = width + 1
    resized_image = np.zeros((height, new_width, 3), dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            if j < seam[i]:
                resized_image[i, j] = image[i, j]
            elif j == seam[i]:
                resized_image[i, j] = image[i, j]
                resized_image[i, j+1] = image[i, j]
            else:
                resized_image[i, j+1] = image[i, j]

    return resized_image