from Face_Detection_and_Histogram_Equalization import face_detection_and_histogram_equalization

def main() -> None:
    """
    Entry point for the face detection and histogram equalization project.
    Calls the main function to process the input image and save the result.
    """
    image_path = "./test_image.png"
    cascade_path = "./haarcascade_frontalface_default.xml"
    face_detection_and_histogram_equalization(image_path, cascade_path)

if __name__ == '__main__':
    main()