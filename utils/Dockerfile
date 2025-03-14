FROM python:3.11
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir flask pillow matplotlib opencv-python easyocr scikit-image scikit-learn scipy

