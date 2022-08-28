import cv2
import numpy as np
import pygame
from pygame import mixer
from pathlib import Path

# camera
camera = cv2.VideoCapture(0)

# pixel_mean variable for storing mean value of all pixels of a frame
pixel_mean = 0

# initialize pygame
pygame.init()

while(True):
    # get current frame of camera
    ret, frame = camera.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

# path folder for loading files
PROJECT_ROOT = Path(__file__).parent.parent

# variable to see if motion is detected or not
detected_motion = False
    # compare mean values of all pixels of 2 consecutive frames, then subtract the 2 mean values
    result = np.abs(np.mean(gray) - pixel_mean) # variable for change in frame
    # change in frame determines motion
    
    # update the pixel mean each time with each new frame
    pixel_mean = np.mean(gray)
    
    # if motion detected, detected_motion is True, and sound will play and let caregivers know that the child has woken up
    if result > 2:
        print("Motion detected!")
        detected_motion = True
        mixer.music.load(PROJECT_ROOT / "Ignition Hacks 2022/0125. Imagination - AShamaluevMusic.mp3")
        mixer.music.play()
    
    # if esc button pressed, then quit
    k = cv2.waitKey(40) & 0xff
    if k == 27:
        break

# end webcam
camera.release()
cv2.destroyAllWindows()
