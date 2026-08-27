import cv2
import serial
import sys
import time

# REPLACED: MediaPipe imports/detector with OpenSeeFace.
sys.path.append("/Users/kamransalahuddin/OpenSeeFace")
from tracker import Tracker

arduinoData = serial.Serial('/dev/cu.usbserial-A5069RR4', 115200)
time.sleep(2)

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
        frame_center_x = img.shape[1] // 2
        frame_center_y = img.shape[0] // 2
        
        face = faces[0]
        # REPLACED: MediaPipe bounding-box center with OpenSeeFace nose landmark.
        nose_y, nose_x, confidence = face.lms[30]

        x = int(nose_x)
        y = int(nose_y)

        error_x = frame_center_x - x
        error_y = frame_center_y - y
        if abs(error_x) < 20:
            error_x = 0

        if abs(error_y) < 20:
            error_y = 0

        cv2.circle(img, (x, y), 6, (0, 0, 255), -1)

        print(x, y)

        send_coordinates_to_arduino(
            int(error_x),
            int(error_y)
        )
    return img
    

