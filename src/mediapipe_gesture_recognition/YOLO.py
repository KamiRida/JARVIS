from ultralytics import YOLO
import cv2
import numpy as np
model = YOLO("yolo26n.pt")
def if_overlap(person_coordinates, object_coordinates):
    overlap_left = max(person_coordinates[0], object_coordinates[0])
    overlap_top = min(person_coordinates[1], object_coordinates[1])
    overlap_right = max(person_coordinates[2], object_coordinates[2])
    overlap_bottom = min(person_coordinates[3], object_coordinates[3])
   
    if overlap_left < overlap_right and overlap_top < overlap_bottom:
        print("Kamran is on his bed")
    else:
        print("Kamran is not on his bed") 

    
def detect_objects(img):
    
    

    # reads frames from a camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = model.track(img)

    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs

    img = result.plot()  # display to screen

    results = model(img, verbose=False)

    dimensions = boxes.xyxy.tolist()
    detected = []
    person_coordinates = []
    object_coordinates = []

    for index, i in enumerate(result.boxes.cls):
        name = result.names[int(i)]
        detected.append(name)

        if name == "person":
            person_coordinates = dimensions[index]

        if name == "bed":
            object_coordinates = dimensions[index]

    if person_coordinates and object_coordinates:
        if_overlap(person_coordinates, object_coordinates)
        print(detected)
        print(dimensions)

    return img

    if cv2.waitKey(1) & 0xff == 27:
        cv2.destroyAllWindows()

