import pygame
import os

def play_sound():
    try:
        pygame.mixer.init()
        sound_file = r"C:\Users\vishn\Desktop\SmartLens\Effect\Listen.mp3"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # Wait for music to finish
            pygame.time.Clock().tick(10)  # Optional: add a small delay to reduce CPU usage
    except Exception as e:
        print(f"Error playing sound: {e}")

