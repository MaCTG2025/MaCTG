'''
Given an image ("./dataset-card.jpg"), develop a system to automatically detect and recognize the car license plate on the image (you can use easyocr for OCR). The system should output the detected license plate region and the recognized text on the license plate. Save the detected region as "detected_plate.png" and the recognized text as "recognized_text.txt".
'''


import cv2
import easyocr
from pathlib import Path
import numpy as np
import os

def load_image(image_path:Path) -> np.ndarray:
    return cv2.imread(str(image_path))

def detect_license_plate(image:np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)
        
        if len(approx) == 4:
            license_plate = approx
            break
    
    return license_plate

def recognize_license_plate(image:np.ndarray, license_plate:np.ndarray) -> str:
    reader = easyocr.Reader(['en'])
    x, y, w, h = cv2.boundingRect(license_plate)
    roi = image[y:y+h, x:x+w]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    thr = cv2.adaptiveThreshold(roi, 252, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, 103, 53)
    roi = cv2.bitwise_not(thr)
    roi = cv2.threshold(roi, 0, 255, cv2.THRESH_OTSU)[1]
    roi = cv2.resize(roi, (1200, 150), interpolation=cv2.INTER_NEAREST)
    # roi = cv2.erode(roi, (3, 3), iterations=3)

    # text = pytesseract.image_to_string(roi, lang='eng', config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 6')
    result = reader.readtext(roi)[0][1]
    
    return result

def main():
    image_path = Path('./dataset-card.jpg')
    image = load_image(image_path)
    
    license_plate = detect_license_plate(image)
    text = recognize_license_plate(image, license_plate)
    
    x, y, w, h = cv2.boundingRect(license_plate)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imwrite('detected_plate.png', image)
    with open('recognized_text.txt', 'w') as f:
        f.write(text)

def test():
    assert Path('detected_plate.png').exists()
    assert Path('recognized_text.txt').exists()
    
    image = cv2.imread('dataset-card.jpg')
    license_plate = detect_license_plate(image)
    x, y, w, h = cv2.boundingRect(license_plate)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    assert np.allclose(cv2.imread('detected_plate.png'), image)

    text = open('recognized_text.txt').read()
    
    assert text == 'CCC 444'

    # cleanup
    # os.remove('detected_plate.png')
    # os.remove('recognized_text.txt')


if __name__ == '__main__':
    # main()
    test()
    print('All tests passed')