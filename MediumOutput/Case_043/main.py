from Face_Detection_and_Background_Blurring import face_detection_and_background_blurring

def main() -> None:
    """
    Entry point for the project. Calls the face_detection_and_background_blurring function to process the image.
    """
    face_detection_and_background_blurring(
        image_path="./test_image.png",
        cascade_path="./haarcascade_frontalface_default.xml",
        scaleFactor=1.1,
        minNeighbors=5,
        blur_kernel_size=(25, 25),
        output_path="final_image.png"
    )

if __name__ == '__main__':
    main()