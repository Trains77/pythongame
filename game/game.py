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
from shared import credits, size, show_debug, disable_background, GameName, block_color, square_size, item_size, player_color, gameIcon, fps, game_border1, game_border2, speed, info_color, dialog_color, background_color
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
Inv_Slot = 0
pygame.mixer.init()
inv = [0, 0, 0, 0]
item1x = 250
item1y = 275
item2y = 300
item2x = 50
if show_debug == True:
    print("Debugging logs enabled")
# Items
hammer_slot = -1
hammer_slot_pos = 235
sword_slot = -1
sword_slot_pos = 235
SelectItem = "NaN"
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

def item_detector(ItemSlotID, ItemID, item_slot, item_slot_pos, posx, posy):
    if inv[ItemSlotID] == 0:
        ItemID = pygame.draw.rect(screen, block_color, [posx,posy,item_size,item_size])
        if pygame.Rect.colliderect(ItemID, player_square) == 1:
            if not Inv_Slot == hammer_slot:
                if not Inv_Slot == sword_slot:
                    Selected_Slot = 150 + 70 * Inv_Slot
                    item_slot_pos = Selected_Slot + 15
                    item_slot = Inv_Slot
                    inv[ItemSlotID] = 1
                    if show_debug == 1:
                        print("Item Get!")
    return item_slot, item_slot_pos

def render_item_inv(item_texture, item_texture2, InvID, ItemSlotPos):
    if inv[InvID] == 1:
        if pygame.Rect.colliderect(inventory_hitbox, player_square) == True:
            image_display(screen, item_texture2, [ItemSlotPos,20])
        elif pygame.Rect.colliderect(inventory_hitbox, player_square) == False:
            image_display(screen, item_texture, [ItemSlotPos,20])

def item_render(ItemSlotID, ItemID, posx, posy, texture):
    SelectedItem = SelectItem
    if inv[ItemSlotID] == 0:
        image_display(screen, texture, [posx,posy])
        SelectedItem = str(SelectItem)
    elif inv[ItemSlotID] == 1:
        if ItemID == Inv_Slot:
            image_display(screen, texture, [playerx + 5,playery + 5])
            SelectedItem = str(ItemSlotID)
        if mouse_button_list[2] == True:
            if not playery + 30 > game_border1:
                if ItemID == Inv_Slot:
                    posx = playerx
                    posy = playery + 30
                    ItemID = -1
                    inv[ItemSlotID] = 0
                    SelectedItem = "NaN"
            elif playery + 30 > game_border1:
                playsound(1,"Audio/Environment/wallhit.wav")
    return posx, posy, ItemID, SelectedItem

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

# The actual Game
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
                    if show_debug == True:
                        print("Quit")
                if event.key == pygame.K_q:
                    if not Inv_Slot == 0:
                        Inv_Slot = Inv_Slot - 1
                        SelectItem = "NaN"
                    elif Inv_Slot == 0:
                        Inv_Slot = 2
                        SelectItem = "NaN"
                if event.key == pygame.K_e:
                    if not Inv_Slot == 2:
                        Inv_Slot = Inv_Slot + 1
                        SelectItem = "NaN"
                    elif Inv_Slot == 2:
                        Inv_Slot = 0
                        SelectItem = "NaN"
            if event.type == pygame.QUIT:
                done = True
                if show_debug == True:
                    print("Quit")

        # Mouse Related info
        cursor_pos = pygame.mouse.get_pos()
        cursory = cursor_pos[1] - 5
        cursorx = cursor_pos[0] - 5
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)

        # Hitbox info
        cursor_square = pygame.draw.rect(screen, block_color, [cursorx, cursory, square_size,square_size])
        square_info = pygame.draw.rect(screen, block_color, [infox,infoy,square_size,square_size])
        player_square = pygame.draw.rect(screen, block_color, [playerx,playery,square_size,square_size])
        player_detector = pygame.draw.rect(screen, block_color, [infox - 5,infoy - 5,square_size + 10,square_size + 10])

        # Item Managment
        hammer_slot, hammer_slot_pos = item_detector(0, "item1", hammer_slot, hammer_slot_pos, item1x, item1y)
        sword_slot, sword_slot_pos = item_detector(1, "item2", sword_slot, sword_slot_pos, item2x, item2y)

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
        if show_debug == True:
            print(facing)

        # Inventory Stuff
        item1x, item1y, hammer_slot, SelectItem = item_render(0, hammer_slot, item1x, item1y, "Textures/items/hammer.png")
        item2x, item2y, sword_slot, SelectItem = item_render(1, sword_slot, item2x, item2y, "Textures/items/sword.png")
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

        render_item_inv("Textures/slot/hammer.png", "Textures/slot/hammer_transparent.png", 0, hammer_slot_pos)
        render_item_inv("Textures/slot/sword.png", "Textures/slot/sword_transparent.png", 1, sword_slot_pos)
        # Dialogs
        if pygame.Rect.colliderect(player_square, player_detector) == 1:
            if SelectItem == "NaN":
                createdialog("Scientist", "Hello User!")
            if SelectItem == "1":
                createdialog("Scientist", "Why are you holding a sword?")
            if SelectItem == "0":
                createdialog("Scientist", "Unfortunatly, you can't do anything with hammers yet")
            if show_debug == True:
                print("Dialog Opened")
#        image_display(screen, "Textures/Environment/tree.png", [infox,infoy])
        if pygame.Rect.colliderect(cursor_square, player_square) == 1:
            createdialog("User", "Hello little mouse!")
            facing = "Down"
            if show_debug == True:
                print("Dialog Opened")

        # Debugging stuff
        if show_debug == True:
            print("Inv_Slot: " + str(Inv_Slot))
            print("Hammer Slot: " + str(hammer_slot))
            print("Sword Slot: " + str(sword_slot))
            print("Hammer POS: " + str(hammer_slot_pos))
            print("Sword POS: " + str(sword_slot_pos))
            print("Held Item: " + SelectItem)
        pygame.display.update()
        pygame.display.flip()
pygame.quit()
exit()
