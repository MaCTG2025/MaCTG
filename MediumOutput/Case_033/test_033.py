'''
Given an image ("./test_image.png"), perform 2 levels of pyramid scaling (upscaling and downscaling). Detect keypoints using ORB (nfeatures = 500) and draw the keypoints(using drawKeypoints) on the upscaled and downscaled images. Finally, save the resulting images as "orb_upscaled.png" and "orb_downscaled.png".
'''

import cv2
from pathlib import Path
import os
import numpy as np
from typing import List

def pyramid_scaling(image_path:Path) -> List[np.ndarray]:
    image = cv2.imread(str(image_path))
    # downscale
    downscale = cv2.pyrDown(image)
    # upscale
    upscale = cv2.pyrUp(image)
    return [upscale, downscale]

def detect_keypoints(image:np.ndarray, nfeatures:int) -> np.ndarray:
    orb = cv2.ORB_create(nfeatures=nfeatures)
    keypoints = orb.detect(image, None)
    return cv2.drawKeypoints(image, keypoints, None)

def main():
    image_path = Path('./test_image.png')
    upscaled, downscaled = pyramid_scaling(image_path)
    orb_upscaled = detect_keypoints(upscaled, 500)
    orb_downscaled = detect_keypoints(downscaled, 500)
    cv2.imwrite('orb_upscaled.png', orb_upscaled)
    cv2.imwrite('orb_downscaled.png', orb_downscaled)

def test():
    assert Path('orb_upscaled.png').exists()
    assert Path('orb_downscaled.png').exists()

    # load the original image
    original = cv2.imread('test_image.png')

    # check downscale
    downscale = cv2.imread('orb_downscaled.png')
    assert downscale.shape[0] == original.shape[0] // 2
    assert downscale.shape[1] == original.shape[1] // 2

    # check upscale
    upscale = cv2.imread('orb_upscaled.png')
    assert upscale.shape[0] == original.shape[0] * 2
    assert upscale.shape[1] == original.shape[1] * 2

    # clean up
    # os.remove('orb_upscaled.png')
    # os.remove('orb_downscaled.png')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')