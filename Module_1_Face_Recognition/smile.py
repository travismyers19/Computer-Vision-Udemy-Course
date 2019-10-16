# Face Recognition

import cv2
import time

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haar_cascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haar_cascade_smile.xml')

# Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame

# Doing some face recognition with the webcam
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.01)

video_capture.release()
cv2.destroyAllWindows()
cv2.waitKey(1)