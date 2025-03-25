from Image_Filtering_and_Saving import image_filtering_and_saving

def main() -> None:
    """
    Entry point for the image filtering and saving process.
    Applies a median filter and a fast mean denoising filter to the input image,
    then saves the processed image to the specified output path.
    """
    input_image_path = "./test_image.png"
    output_image_path = "final_image.png"
    image_filtering_and_saving(input_image_path, output_image_path)

if __name__ == '__main__':
    main()