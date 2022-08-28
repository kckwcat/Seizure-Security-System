import cv2
import numpy as np
import pygame
from pygame import mixer
from pathlib import Path

# camera
camera = cv2.VideoCapture(0)
last_mean = 0

pygame.init()
PROJECT_ROOT = Path(__file__).parent.parent

detected_motion = False
frame_rec_count = 0

while(True):
    # current frame of camera
    ret, frame = camera.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # compare mean values of all pixels of two consecutive frames
    # (subtract two mean values)
    
    result = np.abs(np.mean(gray) - last_mean) # variable for change in frame

    last_mean = np.mean(gray)
    
    # if motion detected
    if result > 2:
        print("Motion detected!")
        detected_motion = True
        mixer.music.load(PROJECT_ROOT / "Ignition Hacks 2022/0125. Imagination - AShamaluevMusic.mp3")
        mixer.music.play()
        
    if detected_motion:
        frame_rec_count = frame_rec_count + 1
    
    # esc button pressed, then quit
    k = cv2.waitKey(40) & 0xff
    if k == 27:
        break

# end webcam
camera.release()
cv2.destroyAllWindows()
