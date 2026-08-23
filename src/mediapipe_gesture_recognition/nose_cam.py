import cv2
import serial
import sys

# REPLACED: MediaPipe imports/detector with OpenSeeFace.
sys.path.append("/Users/kamransalahuddin/OpenSeeFace")
from tracker import Tracker

arduinoData = serial.Serial('/dev/cu.usbserial-A5069RR4', 9600)

def send_coordinates_to_arduino(x, y):
    coordinates = f"{x},{y}\r"
    arduinoData.write(coordinates.encode())
    print(f"X{x}Y{y}\n")

def track_nose(img, tracker):
# REPLACED: OpenSeeFace needs the frame size when creating the tracker.

    # REPLACED: MediaPipe face detection with OpenSeeFace tracking.
    faces = tracker.predict(img)
    print("faces detected:", len(faces))

    if len(faces) > 0:
        face = faces[0]
        # REPLACED: MediaPipe bounding-box center with OpenSeeFace nose landmark.
        nose_y, nose_x, confidence = face.lms[30]

        x = int(nose_x)
        y = int(nose_y)

        cv2.circle(img, (x, y), 6, (0, 0, 255), -1)

        

        send_coordinates_to_arduino(
            int(x),
            int(y)
        )
    return img


