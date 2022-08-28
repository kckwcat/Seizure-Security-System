import cv2
import pyaudio
import numpy as np
import pygame
from pygame import mixer
from pathlib import Path

pygame.init()
PROJECT_ROOT = Path(__file__).parent.parent

cap = cv2.VideoCapture(0)
last_mean = 0

motion_detected = False
frame_rec_count = 0


while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = np.abs(np.mean(gray) - last_mean)
    #print(result)
    last_mean = np.mean(gray)
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    buffer = []
    string_audio_data = stream.read(CHUNK)
    audio_data = np.frombuffer(string_audio_data, np.int16)
    volume_norm = np.linalg.norm(audio_data)*10
    dfft = 10.*np.log10(abs(np.fft.rfft(audio_data)))
    if volume_norm > 900000:
        mixer.music.load(PROJECT_ROOT / "Ignition Hacks 2022/mixkit-alarm-digital-clock-beep-989.wav")
        mixer.music.play()
        
    else:
        mixer.music.pause()
    
    
    #print(result)
    if result > 20:
        print("Motion detected!")
        #print("Started recording.")
        motion_detected = True
    else:
        motion_detected = False
        
        
    if motion_detected:
        #out.write(frame)
        mixer.music.load(PROJECT_ROOT / "Ignition Hacks 2022/0125. Imagination - AShamaluevMusic.mp3")
        mixer.music.play()
        frame_rec_count = frame_rec_count + 1
        
    else:
        mixer.music.pause()
        
    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break

cap.release()
cv2.destroyAllWindows()
