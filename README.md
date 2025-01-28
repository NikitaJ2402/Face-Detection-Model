# Face-Detection-Model
Overview
This project demonstrates real-time face detection using OpenCV's Haar Cascade Classifier. The model utilizes a pre-trained haarcascade_frontalface_default.xml file to identify faces in images and video streams. The project is suitable for learning about computer vision techniques, basic face detection algorithms, and working with OpenCV.

Features
Real-time Face Detection: Detect faces in live video streams from the webcam.
Face Highlighting: Automatically draws bounding boxes around detected faces.
Customizable Parameters: Adjust detection accuracy with parameters like scaleFactor and minNeighbors.

How It Works
Haar Cascade Classifier: The project employs OpenCV's Haar Cascade Classifier, a machine learning-based approach for object detection.
Video Capture: Frames are captured in real-time from the webcam.
Face Detection: The grayscale version of each frame is processed to detect faces.
Display: Bounding boxes are drawn around detected faces and displayed in a live video feed.

Prerequisites
Python 3.x
OpenCV library (pip install opencv-python and opencv-python-headless)

Code Highlights
Image-Based Face Detection: Detect faces in a static image and save the output with highlighted faces.
Live Face Detection: Detect faces in real-time using webcam input.
