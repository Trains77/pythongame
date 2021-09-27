# Script Modules
import platform
import sys
# import getpass
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
from time import sleep
from shared import credits, size, GameName, square_size, player_color, game_border1, game_border2, speed, info_color, dialog_color, background_color
from colored import fore, back, style
import math
import random
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)
# Credits
import credits
# Display
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
clock = pygame.time.Clock()
# Player Position
playerx = int(math.ceil(random.randint(10,450) / 10.0)) * 10
playery = int(math.ceil(random.randint(10,450) / 10.0)) * 10
# Game
while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.
        clock.tick(10)
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not playerx == game_border2:
                        playerx = playerx - speed
                if event.key == pygame.K_RIGHT:
                    if not playerx == game_border1:
                        playerx = playerx + speed
                if event.key == pygame.K_UP:
                    if not playery == game_border2:
                        playery = playery - speed
                if event.key == pygame.K_DOWN:
                    if not playery == game_border1:
                        playery =playery + speed
            if event.type == pygame.QUIT:
                done = True
        player_square = pygame.draw.rect(screen, background_color, [playerx,playery,square_size,square_size])
        player_detector = pygame.draw.rect(screen, background_color, [195,195,square_size + 10,square_size + 10])
        image_display(screen, "Textures/npc.png", [playerx,playery])
        square_info = pygame.draw.rect(screen, info_color, [200,200,square_size,square_size])
        if pygame.Rect.colliderect(player_square, player_detector) == 1:
            dialog_box = pygame.draw.rect(screen, dialog_color, [10,350,480,140])
            font1 = pygame.font.SysFont('Nerds', 20)
            img1 = font1.render('Testing Square:', True, BLACK)
            img2 = font1.render('Hello User!', True, BLACK)
            screen.blit(img1, (15, 360))
            screen.blit(img2, (30, 390))
        pygame.display.update()
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
