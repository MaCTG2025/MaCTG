import cv2
import numpy as np

def process_image(image_path: str, cascade_path: str, scaleFactor: float = 1.1, minNeighbors: int = 5, blur_kernel_size: tuple = (25, 25), output_path: str = "final_image.png") -> None:
    """
    Detects faces in the input image using Haar cascades, applies Gaussian blur to the background, and saves the resulting image.

    Args:
        image_path (str): Path to the input image file (e.g., "./test_image.png").
        cascade_path (str): Path to the Haar cascade XML file (e.g., "./haarcascade_frontalface_default.xml").
        scaleFactor (float, optional): Parameter specifying how much the image size is reduced at each image scale. Defaults to 1.1.
        minNeighbors (int, optional): Parameter specifying how many neighbors each candidate rectangle should have to retain it. Defaults to 5.
        blur_kernel_size (tuple, optional): Size of the Gaussian blur kernel (width, height). Defaults to (25, 25).
        output_path (str, optional): Path to save the resulting image. Defaults to "final_image.png".

    Returns:
        None: The function saves the processed image to the specified output path.

    Steps:
        1. Load the input image from `image_path`.
        2. Load the Haar cascade classifier from `cascade_path`.
        3. Detect faces in the image using the Haar cascade with the specified `scaleFactor` and `minNeighbors`.
        4. Create a mask for the detected faces.
        5. Apply Gaussian blur to the entire image using the specified `blur_kernel_size`.
        6. Use the face mask to restore the original face regions in the blurred image.
        7. Save the resulting image to `output_path`.

    Example:
        process_image("./test_image.png", "./haarcascade_frontalface_default.xml", scaleFactor=1.1, minNeighbors=5, blur_kernel_size=(25, 25), output_path="final_image.png")
    """
    # Load the input image
    image = cv2.imread(image_path)
    
    # Load the Haar cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    
    # Create a mask for the detected faces
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    for (x, y, w, h) in faces:
        cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)
    
    # Apply Gaussian blur to the entire image
    blurred_image = cv2.GaussianBlur(image, blur_kernel_size, 0)
    
    # Restore the original face regions in the blurred image
    result_image = cv2.bitwise_and(blurred_image, blurred_image, mask=cv2.bitwise_not(mask))
    result_image = cv2.add(result_image, cv2.bitwise_and(image, image, mask=mask))
    
    # Save the resulting image
    cv2.imwrite(output_path, result_image)