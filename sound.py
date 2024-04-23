import pygame
import os

class Sound:
    def __init__(self):
        chemin_musique = os.path.join(os.getcwd(), "sounds", "son_zelda.ogg")
        pygame.mixer.music.load(chemin_musique)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()