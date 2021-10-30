# Script Modules
import platform
import sys
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
from time import sleep
from shared import credits, size, disable_background, GameName, block_color, square_size, item1x, item1y, item_size, player_color, gameIcon, fps, game_border1, game_border2, speed, info_color, dialog_color, background_color
from colored import fore, back, style
import math
import random
# Default Variables
infox = 200
infoy = 200
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
Inv_Slot = 1
pygame.mixer.init()
inv = [0, 0, 0, 0]
hammer_slot = 1
hammer_slot_pos = 235
# Functions
def createdialog(speaker, text):
    dialog_box = pygame.draw.rect(screen, dialog_color, [10,350,480,140])
    font1 = pygame.font.SysFont('Nerds', 20)
    img1 = font1.render(speaker + ":", True, BLACK)
    img2 = font1.render(text, True, BLACK)
    screen.blit(img1, (15, 360))
    screen.blit(img2, (30, 390))
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)
def playsound(channel,audiofile):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(audiofile))

# Credits
import credits

# Display
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
# Player Position
playerx = int(math.ceil(random.randint(10,450) / 10.0)) * 10
playery = int(math.ceil(random.randint(10,450) / 10.0)) * 10
# Game
facing = "Right"
while not done:
        clock.tick(fps)
        screen.fill(background_color)
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        inventory_hitbox = pygame.draw.rect(screen, (255,255,255), [140, 5, 220, 60])
        Selected_Slot = 150 + 70 * Inv_Slot
        # Controls
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if not playerx == game_border2:
                        playerx = playerx - speed
                    elif playerx == game_border2:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Left"
                if event.key == pygame.K_d:
                    if not playerx == game_border1:
                        playerx = playerx + speed
                    elif playerx == game_border1:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Right"
                if event.key == pygame.K_w:
                    if not playery == game_border2:
                        playery = playery - speed
                    elif playery == game_border2:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Up"
                if event.key == pygame.K_s:
                    if not playery == game_border1:
                        playery =playery + speed
                    elif playery == game_border1:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Down"
                if event.key == pygame.K_LEFT:
                    if not playerx == game_border2:
                        playerx = playerx - speed
                    elif playerx == game_border2:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Left"
                if event.key == pygame.K_RIGHT:
                    if not playerx == game_border1:
                        playerx = playerx + speed
                    elif playerx == game_border1:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Right"
                if event.key == pygame.K_UP:
                    if not playery == game_border2:
                        playery = playery - speed
                    elif playery == game_border2:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Up"
                if event.key == pygame.K_DOWN:
                    if not playery == game_border1:
                        playery =playery + speed
                    elif playery == game_border1:
                        playsound(1,"Audio/Environment/wallhit.wav")
                    facing = "Down"
                if event.key == pygame.K_ESCAPE:
                    done = True
                    print("Quit")
                if event.key == pygame.K_q:
                    if not Inv_Slot == 0:
                        Inv_Slot = Inv_Slot - 1
                    elif Inv_Slot == 0:
                        Inv_Slot = 2
                if event.key == pygame.K_e:
                    if not Inv_Slot == 2:
                        Inv_Slot = Inv_Slot + 1
                    elif Inv_Slot == 2:
                        Inv_Slot = 0
            if event.type == pygame.QUIT:
                done = True
                print("Quit")

        # Mouse Related info
        cursor_pos = pygame.mouse.get_pos()
        cursory = cursor_pos[1] - 5
        cursorx = cursor_pos[0] - 5
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        button_pressed = any(mouse_button_list)

        # Hitbox info
        cursor_square = pygame.draw.rect(screen, block_color, [cursorx, cursory, square_size,square_size])
        square_info = pygame.draw.rect(screen, block_color, [infox,infoy,square_size,square_size])
        player_square = pygame.draw.rect(screen, block_color, [playerx,playery,square_size,square_size])
        player_detector = pygame.draw.rect(screen, block_color, [infox - 5,infoy - 5,square_size + 10,square_size + 10])

        # Item Managment
        if inv[0] == 0:
            item1 = pygame.draw.rect(screen, block_color, [item1x,item1y,item_size,item_size])
            if pygame.Rect.colliderect(item1, player_square) == 1:
                inv[0] = 1
                print("Item Get!")
                hammer_slot_pos = Selected_Slot + 15
                hammer_slot = Inv_Slot
        # Background and players
        if disable_background == False:
            image_display(screen, "Textures/Environment/background.png", [0,0])
        if facing == "Left":
            image_display(screen, "Textures/Characters/Player/playerflipped.png", [playerx,playery])
        elif facing == "Right":
            image_display(screen, "Textures/Characters/Player/player.png", [playerx,playery])
        elif facing == "Up":
            image_display(screen, "Textures/Characters/Player/playerup.png", [playerx,playery])
        elif facing == "Down":
            image_display(screen, "Textures/Characters/Player/playerdown.png", [playerx,playery])
        if playerx > infox:
            image_display(screen, "Textures/Characters/Scientist/scientist.png", [infox,infoy])
        elif playerx < infox:
            image_display(screen, "Textures/Characters/Scientist/scientist_flipped.png", [infox,infoy])
        elif playerx == infox:
            if playery > infoy:
                image_display(screen, "Textures/Characters/Scientist/scientist_down.png", [infox,infoy])
            elif playery < infoy:
                image_display(screen, "Textures/Characters/Scientist/scientist_up.png", [infox,infoy])

        # Inventory Stuff
        if inv[0] == 0:
            image_display(screen, "Textures/items/hammer.png", [item1x,item1y])
        elif inv[0] == 1:
            image_display(screen, "Textures/items/hammer.png", [playerx + 5,playery + 5])
            if mouse_button_list[1] == True:
                if not playery + 30 > game_border1:
                    if hammer_slot == Inv_Slot:
                        item1x = playerx
                        item1y = playery + 30
                        inv[0] = 0
                elif playery + 30 > game_border1:
                    print("Player tried to place item beyond maximum range")
                    playsound(1,"Audio/Environment/wallhit.wav")
        if pygame.Rect.colliderect(inventory_hitbox, player_square) == True:
            if Inv_Slot == 1:
                image_display(screen,"Textures/slot/icon_select_transparent.png", [220, 5])
            elif not Inv_Slot == 1:
                image_display(screen,"Textures/slot/icon_unselect_transparent.png", [220, 5])
            if Inv_Slot == 0:
                image_display(screen,"Textures/slot/icon_select_transparent.png", [150, 5])
            elif not Inv_Slot == 0:
                image_display(screen,"Textures/slot/icon_unselect_transparent.png", [150, 5])
            if Inv_Slot == 2:
                image_display(screen,"Textures/slot/icon_select_transparent.png", [290, 5])
            elif not Inv_Slot == 2:
                image_display(screen,"Textures/slot/icon_unselect_transparent.png", [290, 5])
        elif pygame.Rect.colliderect(inventory_hitbox, player_square) == False:
            if Inv_Slot == 1:
                image_display(screen,"Textures/slot/icon_select.png", [220, 5])
            elif not Inv_Slot == 1:
                image_display(screen,"Textures/slot/icon_unselect.png", [220, 5])
            if Inv_Slot == 0:
                image_display(screen,"Textures/slot/icon_select.png", [150, 5])
            elif not Inv_Slot == 0:
                image_display(screen,"Textures/slot/icon_unselect.png", [150, 5])
            if Inv_Slot == 2:
                image_display(screen,"Textures/slot/icon_select.png", [290, 5])
            elif not Inv_Slot == 2:
                image_display(screen,"Textures/slot/icon_unselect.png", [290, 5])
        if inv[0] == 1:
            if pygame.Rect.colliderect(inventory_hitbox, player_square) == True:
                image_display(screen, "Textures/slot/hammer_transparent.png", [hammer_slot_pos,20])
            elif pygame.Rect.colliderect(inventory_hitbox, player_square) == False:
                image_display(screen, "Textures/slot/hammer.png", [hammer_slot_pos,20])

        # Dialogs
        if pygame.Rect.colliderect(player_square, player_detector) == 1:
            createdialog("Scientist", "Hello User!")
        image_display(screen, "Textures/Environment/tree.png", [infox,infoy])
        if pygame.Rect.colliderect(cursor_square, player_square) == 1:
            createdialog("User", "Hello little mouse!")
            facing = "Down"
        pygame.display.update()
        pygame.display.flip()
# Quite the execution when clicking on close
pygame.quit()
exit()
