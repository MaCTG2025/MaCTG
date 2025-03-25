import cv2
import numpy as np

def detect_and_draw_corners(image: np.array, max_corners: int = 100, quality_level: float = 0.01, 
                            min_distance: int = 10, color: tuple = (0, 0, 255), radius: int = 3, 
                            thickness: int = -1) -> np.array:
    """
    Detects corners in an image and draws them with specified parameters.

    Args:
        image (np.array): The input image in which corners are to be detected.
        max_corners (int, optional): Maximum number of corners to detect. Defaults to 100.
        quality_level (float, optional): Parameter characterizing the minimal accepted quality of image corners. 
                                         Defaults to 0.01.
        min_distance (int, optional): Minimum possible Euclidean distance between the returned corners. 
                                      Defaults to 10.
        color (tuple, optional): Color of the drawn corners in BGR format. Defaults to (0, 0, 255) (red).
        radius (int, optional): Radius of the circle representing the corners. Defaults to 3.
        thickness (int, optional): Thickness of the circle outline. If -1, the circle is filled. Defaults to -1.

    Returns:
        np.array: The image with detected corners drawn on it.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray_image, maxCorners=max_corners, qualityLevel=quality_level, minDistance=min_distance)
    corners = corners.astype(np.int32)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(image, (x, y), radius, color, thickness)

    return image