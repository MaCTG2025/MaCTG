from Dynamic_Color_Filtering import dynamic_color_filter_module

def main() -> None:
    """
    Entry point for the dynamic color filtering project. Processes the input image
    './test_image.png' by applying dynamic color filtering based on pixel brightness
    and saves the result as 'filtered_image.png'.
    """
    dynamic_color_filter_module('./test_image.png', brightness_threshold=150)

if __name__ == '__main__':
    main()