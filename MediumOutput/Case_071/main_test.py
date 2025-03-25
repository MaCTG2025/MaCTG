import unittest
from main import main
import numpy as np
from unittest.mock import patch, MagicMock

class TestMainFunction(unittest.TestCase):

    @patch('main.load_images')
    @patch('main.transform_object_image')
    @patch('main.seamless_cloning')
    @patch('main.save_image')
    def test_main_function(self, mock_save_image, mock_seamless_cloning, mock_transform_object_image, mock_load_images):
        # Mocking the return values of the helper functions
        mock_background = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_object_img = np.zeros((50, 50, 3), dtype=np.uint8)
        mock_transformed_object = np.zeros((50, 50, 3), dtype=np.uint8)
        mock_blended_image = np.zeros((100, 100, 3), dtype=np.uint8)

        mock_load_images.side_effect = [mock_background, mock_object_img]
        mock_transform_object_image.return_value = mock_transformed_object
        mock_seamless_cloning.return_value = mock_blended_image

        # Calling the main function with mock paths
        main('background.jpg', 'object.jpg', 'output.jpg')

        # Asserting that all helper functions were called with the correct arguments
        mock_load_images.assert_any_call('background.jpg')
        mock_load_images.assert_any_call('object.jpg')
        mock_transform_object_image.assert_called_once_with(mock_object_img)
        mock_seamless_cloning.assert_called_once_with(mock_transformed_object, mock_background)
        mock_save_image.assert_called_once_with(mock_blended_image, 'output.jpg')

    @patch('main.load_images')
    @patch('main.transform_object_image')
    @patch('main.seamless_cloning')
    @patch('main.save_image')
    def test_main_function_error_handling(self, mock_save_image, mock_seamless_cloning, mock_transform_object_image, mock_load_images):
        # Simulate an error in load_images
        mock_load_images.side_effect = Exception("Error loading images")

        # Calling the main function with mock paths
        with self.assertRaises(Exception):
            main('background.jpg', 'object.jpg', 'output.jpg')

if __name__ == '__main__':
    unittest.main()