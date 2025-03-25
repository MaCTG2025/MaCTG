'''
Given an image ("./test_image.png"), compute HOG features (cellSize = 8x8, blockSize = 2x2, nbins = 9) and compute the Local Binary Pattern features. Save the HOG features as "hog_features.npy" and the LBP features as "lbp_features.npy".
'''

import cv2
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def compute_hog_features(image:np.ndarray, cellSize:tuple, blockSize:tuple, nbins:int) -> np.ndarray:
    hog = cv2.HOGDescriptor(_winSize=(image.shape[1] // cellSize[1] * cellSize[1],
                                      image.shape[0] // cellSize[0] * cellSize[0]),
                            _blockSize=(blockSize[1] * cellSize[1],
                                        blockSize[0] * cellSize[0]),
                            _blockStride=(cellSize[1], cellSize[0]),
                            _cellSize=(cellSize[1], cellSize[0]),
                            _nbins=nbins)
    n_cells = (image.shape[0] // cellSize[0], image.shape[1] // cellSize[1])
    hog_feats = hog.compute(image).reshape(n_cells[1] - blockSize[1] + 1,
                                           n_cells[0] - blockSize[0] + 1,
                                           blockSize[0], blockSize[1], nbins).transpose((1, 0, 2, 3, 4))
    gradients = np.zeros((n_cells[0], n_cells[1], nbins))
    cell_count = np.full((n_cells[0], n_cells[1], 1), 0, dtype=int)
    for off_y in range(blockSize[0]):
        for off_x in range(blockSize[1]):
            gradients[off_y:n_cells[0] - blockSize[0] + off_y + 1,
                      off_x:n_cells[1] - blockSize[1] + off_x + 1] += hog_feats[:, :, off_y, off_x, :]
            cell_count[off_y:n_cells[0] - blockSize[0] + off_y + 1,
                       off_x:n_cells[1] - blockSize[1] + off_x + 1] += 1
    gradients /= cell_count
    return gradients


def compute_lbp_features(image:np.ndarray) -> np.ndarray:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h, w = gray_image.shape
    lbp = np.zeros((h-2, w-2), dtype=np.uint8)
    for y in range(1, h-1):
        for x in range(1, w-1):
            center = gray_image[y, x]
            code = 0
            code |= (gray_image[y-1, x-1] > center) << 7
            code |= (gray_image[y-1, x] > center) << 6
            code |= (gray_image[y-1, x+1] > center) << 5
            code |= (gray_image[y, x+1] > center) << 4
            code |= (gray_image[y+1, x+1] > center) << 3
            code |= (gray_image[y+1, x] > center) << 2
            code |= (gray_image[y+1, x-1] > center) << 1
            code |= (gray_image[y, x-1] > center) << 0
            lbp[y-1, x-1] = code
    return lbp


def main():
    image_path = Path('./test_image.png')
    image = load_image(image_path)
    hog_features = compute_hog_features(image, (8, 8), (2, 2), 9)
    lbp_features = compute_lbp_features(image)
    np.save('hog_features.npy', hog_features)
    np.save('lbp_features.npy', lbp_features)

def test():
    assert Path('hog_features.npy').exists()
    assert Path('lbp_features.npy').exists()

    image = load_image(Path('./test_image.png'))
    hog_features = compute_hog_features(image, (8, 8), (2, 2), 9)
    lbp_features = compute_lbp_features(image)
    result_hog = np.load('hog_features.npy')
    result_lbp = np.load('lbp_features.npy')
    assert np.array_equal(hog_features, result_hog)
    assert np.array_equal(lbp_features, result_lbp)

    # clean up
    # os.remove('hog_features.npy')
    # os.remove('lbp_features.npy')

if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')