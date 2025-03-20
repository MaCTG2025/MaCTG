from Image_Processing_and_Edge_Detection import image_processing_and_edge_detection

def main() -> None:
    """
    Entry point for the project. Calls the image processing and edge detection function.

    Inputs:
        None

    Output:
        None
    """
    image_processing_and_edge_detection("./test_image.png", "sobel_edges.png", kernel_size=3)

if __name__ == '__main__':
    main()