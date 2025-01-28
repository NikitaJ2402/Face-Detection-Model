# import cv2

# # Load the image
# img = cv2.imread("D:\IMG_20231130_214341.jpg")

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Use Haar cascades to detect faces
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# # Save the image to view it
# cv2.imwrite('output.jpg', img)
# print("Image saved as 'output.jpg'")




import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video from the webcam
video_capture = cv2.VideoCapture(0)  # 0 is the default webcam, use 1 or 2 if you have multiple cameras

while True:
    # Read the current frame from the video stream
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture video. Exiting...")
        break

    # Convert the frame to grayscale (Haar cascades work on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with the rectangles
    cv2.imshow('Live Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):                             #break the window 
        break

# Release the webcam and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
