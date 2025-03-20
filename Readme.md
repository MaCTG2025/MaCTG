# MaCTG

## Run MaCTG
### Install dependencies
```shell
pip install -r requirements.txt
```
### Create API file
```shell
# in repo folder, create a file containing your own DeepSeek API key
vim deepseek_api
```

### Run MaCTG
```shell
python run_ds.py
```

## Sample Output
Here are some output samples of MaCTG.
| Case_number | Input_image | Requirement                                                                                                                                                                                                                                                                                                                                                                       | Output_image |
|-------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 001         | <img src="./SimpleOutput/Case_001/squares.jpg" width="100" height="100" />            | Given an input image ("./squares.jpg"), find all corners of the squares in the image and draw them as red circles(radius=3) on the image. Save the image as "squares_with_corners.png".<br>                                                                                                                                                                                       |   <img src="./SimpleOutput/Case_001/squares_with_corners.png" width="100" height="100" />           |
| 013         |<img src="./SimpleOutput/Case_013/test_image.png" width="100" height="100" />| Given an input image ("./test_image.png") and a face cascade file ("./haarcascade_frontalface_default.xml"), detect the face (only one) in the image and draw a rectangle (in red, thickness=2) around it. Save the resulting image as "face_detected.png".                                                                                                                       |<img src="./SimpleOutput/Case_013/face_detected.png" width="100" height="100" />|
| 018         |<img src="SimpleOutput/Case_018/someshapes.jpg" width="100" height="100" />| Given an input image ("./someshapes.jpg"), there is a rectangle, a square, a triangle, a circle and a star in the image. Find these shapes and draw the contours of the shape in different colors (thickness=2): red for the rectangle, green for the square, blue for the triangle, yellow for the circle and pink for the star. Save the resulting image as "shapes_image.png". |<img src="SimpleOutput/Case_018/shapes_image.png" width="100" height="100" />|
