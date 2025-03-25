from Image_Processing_Pipeline import image_processing_pipeline

def main() -> None:
    """
    Entry point for the image processing pipeline. Processes the input image and saves the result.
    """
    image_processing_pipeline("./test_image.png", output_path="test_image_edges.png")

if __name__ == '__main__':
    main()