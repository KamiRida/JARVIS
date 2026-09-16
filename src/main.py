import cv2
from mediapipe_gesture_recognition.nose_cam import track_nose, send_coordinates_to_arduino
from ultralytics import YOLO
from mediapipe_gesture_recognition.YOLO import detect_objects
#from tracker import Tracker
from mediapipe_gesture_recognition.hand_tracker import run_hand_tracker
 
model = YOLO("yolo26n.pt")

webcam = cv2.VideoCapture(0)
ret, img = webcam.read()

img_h, img_w = img.shape[:2]

# tracker = Tracker(
#     img_w,
#     img_h,
#     model_type=3,
#     max_faces=1,
#     no_gaze=True,
#     silent=True,
#     detection_threshold=0.1,
#     try_hard=True
# )

while True:

    ret, img = webcam.read()
    img = cv2.rotate(img, cv2.ROTATE_180)

    if not ret:
        continue
    img = detect_objects(img)
    #img = track_nose(img, tracker=tracker)
    img = run_hand_tracker(img)
    cv2.imshow("Jarvis", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
