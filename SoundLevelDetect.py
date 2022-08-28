import pyaudio
import numpy as np
import pygame

pygame.init()

# alarm sound module
alarm_sound = pygame.mixer.Sound("mixkit-alarm-digital-clock-beep-989.wav")

# alarm sound function
def alert_sound():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while True:
        # read audio data
        str_audio_data = stream.read(CHUNK)
        audio_data = np.frombuffer(str_audio_data, np.int16)
        volume_detected = np.linalg.norm(audio_data)*10
        
        # if possible seizure detected, alarm will sound
        # I don't know the exact number of decibels for a seizure sound, so I just shouted to decide the value (volume level) for volume_detected to compare to
        if volume_detected > 900000:
            print('oh no')
            alarm_sound.set_volume(0.8)
            pygame.mixer.Sound.play(alarm_sound)


alert_sound()
