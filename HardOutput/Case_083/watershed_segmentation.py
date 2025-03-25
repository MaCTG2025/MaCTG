import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage

def watershed_segmentation(input_image_path: str, output_image_path: str) -> None:
    """
    Perform image segmentation using the Watershed method.

    This function reads an image from the specified input path, applies the Watershed algorithm
    to segment the image into distinct regions based on intensity gradients, and saves the
    segmented image to the specified output path. Over-segmentation is handled using markers.

    Parameters:
    -----------
    input_image_path : str
        The file path to the input image (e.g., "./water_coins.jpg").
    output_image_path : str
        The file path where the segmented image will be saved (e.g., "water_coins_segmented.png").

    Returns:
    --------
    None
        The function does not return any value. It saves the segmented image to the specified output path.

    Dependencies:
    -------------
    - OpenCV (cv2)
    - NumPy (np)
    - scikit-image (skimage.feature.peak_local_max, skimage.segmentation.watershed)
    - SciPy (scipy.ndimage)

    Steps:
    ------
    1. Read the input image in grayscale.
    2. Apply a binary threshold to create a binary image.
    3. Compute the Euclidean Distance Transform (EDT) of the binary image.
    4. Identify local maxima in the EDT to use as markers for the Watershed algorithm.
    5. Apply the Watershed algorithm to segment the image.
    6. Save the segmented image to the specified output path.

    Example:
    --------
    watershed_segmentation("./water_coins.jpg", "water_coins_segmented.png")
    """
    # Read the input image in grayscale
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Apply a binary threshold to create a binary image
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Compute the Euclidean Distance Transform (EDT) of the binary image
    edt = ndimage.distance_transform_edt(binary_image)

    # Identify local maxima in the EDT to use as markers for the Watershed algorithm
    markers = peak_local_max(edt, footprint=np.ones((3, 3)), min_distance=20, labels=binary_image)

    # Label the markers
    markers = ndimage.label(markers)[0]

    # Apply the Watershed algorithm to segment the image
    segmentation = watershed(-edt, markers, mask=binary_image)

    # Convert the segmentation result to RGB for visualization
    segmentation_rgb = np.zeros_like(image, dtype=np.uint8)
    segmentation_rgb[segmentation == 0] = [255, 255, 255]
    for i in range(1, len(np.unique(segmentation))):
        segmentation_rgb[segmentation == i] = np.random.randint(0, 256, size=(3,)).tolist()

    # Save the segmented image to the specified output path
    cv2.imwrite(output_image_path, segmentation_rgb)