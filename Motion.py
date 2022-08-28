import cv2
import numpy as np

# camera
camera = cv2.VideoCapture(0)
last_mean = 0

detected_motion = False
frame_rec_count = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')

first_val = True

while(True):
        
    # current frame of camera
    ret, frame = camera.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = np.abs(np.mean(gray) - last_mean)

    last_mean = np.mean(gray)

    if result > 1:
        print("Motion detected!")
        detected_motion = True
    if detected_motion:
        frame_rec_count = frame_rec_count + 1
        
    k = cv2.waitKey(40) & 0xff
    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()
