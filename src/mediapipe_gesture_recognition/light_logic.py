import mediapipe_gesture_recognition.tp_link as tp_link
import time
import asyncio
last_gesture = ""
none_start_time = None
elapsed = None
def light_logic(latest_gesture):
    global last_gesture
    global elapsed
    global none_start_time
    if latest_gesture == "None" and none_start_time is None:
        none_start_time = time.time()
    if latest_gesture != "None":
        none_start_time = None
    if latest_gesture == "None":
        elapsed = time.time() - none_start_time
    if latest_gesture == "None" and elapsed != None and elapsed > 0.3:
        last_gesture = "None"

    #Turning on and off right lamp

    if latest_gesture == "Pointing_Up" and last_gesture != latest_gesture: 
        asyncio.run(tp_link.right_turn_on())
        last_gesture = latest_gesture
        none_start_time = None
    if latest_gesture == "Closed_Fist" and last_gesture == "Pointing_Up":         
        asyncio.run(tp_link.right_turn_off())        
        last_gesture = latest_gesture
        none_start_time = None

    
