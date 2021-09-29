from time import sleep
import os
from shared import song, credits
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pydub
from pygame.locals import *
from shared import enable_music
if enable_music == 1:
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
#    pygame.mixer.Channel(0).play(pygame.mixer.Sound(song))
# background music which is owned by FesliyanStudios.
