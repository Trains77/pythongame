# This script was made on Linux, it may not work on other operating systems

# Script Modules
import platform
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
import time
from shared import *
from colored import fore, back, style
import math
import random
pygame.mixer.init()

# The Credits
print(fore.BLUE)
print("Program by Trains77")
print()
print("Artwork by Trains77")
print()
print("Background Music: https://www.FesliyanStudios.com and")
print("                  https://freemusicarchive.org/music/defrini")
print()
print("Made with Atom Editor")
print()
print("Utilizes Pygame")
print()
print("AnotherGame " + version)
print(style.RESET)

if not platform.system() == system_recommends:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this program" + style.RESET)
if enable_program == True:
    done = False
elif enable_program == False:
    print("The program has been disabled in shared.py")
    print()
    print(fore.WHITE + back.RED + style.BOLD + "ERROR: GAME_DISABLED" + style.RESET)
    done = True

def createdialog(speaker, text):
    dialog_box = pygame.draw.rect(screen, dialog_color, [10,350,480,140])
    img1 = font1.render(speaker + ":", True, BLACK)
    img2 = font1.render(text, True, BLACK)
    img3 = font1.render("Press 'z' to continue", True, BLACK)
    screen.blit(img1, (15, 360))
    screen.blit(img2, (30, 390))
    screen.blit(img3, (355, 470))
def poison_effect():
    healths = health
    poison = poison_duration
    if health_tick == 19:
        if poison > 0:
            healths = deal_damage(1)
            poison = poison - 1
    return poison, healths
def create_notice(posx, posy):
    img4 = pygame.image.load(characters_path + "speaking.png")
    screen.blit(img4, [posx, posy - 20])

def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)

def playsound(channel,audiofile):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(audiofile))
def health_bar():
    if poison_duration > 0:
        health_color = GREEN
    else:
        health_color = RED
    health_ticks = health_tick + 1
    if health < max_health / 4 + 1:
        if health_ticks < 10:
            health_color = BLACK
        elif health_ticks > 10:
            if poison_duration > 0:
                health_color = GREEN
            else:
                health_color = RED
        else:
            if poison_duration > 0:
                health_color = GREEN
            else:
                health_color = RED
    if health_ticks == 20:
        health_ticks = 0
    health_txt = font1.render("Health: " + str(health) + "/" + str(max_health), True, BLACK)
    screen.blit(health_txt, (20, 470))
    if dead == False:
        create_square(GRAY, 9, 484, 6 * max_health + 1, 12)
    for i in range(health):
        if dead == False:
            create_square(health_color, 10 + 6 * i, 485, 5, 10)
    return health_ticks

def item_detector(ItemSlotID, ItemID, item_slot, item_slot_pos, posx, posy):
    if item_world_id[ItemSlotID] == mapid:
        if inv[ItemSlotID] == 0:
            ItemID = pygame.draw.rect(screen, block_color, [posx,posy,item_size,item_size])
            if pygame.Rect.colliderect(ItemID, player_square) == 1:
                if SelectItem == "NaN":
                    Selected_Slot = 80 + 70 * Inv_Slot
                    item_slot_pos = Selected_Slot + 15
                    item_slot = Inv_Slot
                    inv[ItemSlotID] = 1
                    if show_debug == 1:
                        print("Item Get!")
                    playsound(1, environment_audio_path + "pickup.wav")
    return item_slot, item_slot_pos

def render_item_inv(item_texture, InvID, ItemSlot, ItemSlotPos):
    if inv[InvID] == 1:
        if pygame.Rect.colliderect(inventory_hitbox, player_square) == True:
            image_display(screen, inventory_path + transparent_prefix + item_texture, [ItemSlotPos,20])
        elif pygame.Rect.colliderect(inventory_hitbox, player_square) == False:
            image_display(screen, inventory_path + item_texture, [ItemSlotPos,20])
        if ItemSlot == Inv_Slot:
            if item_texture == "axe.png":
                item_name = font1.render("Axe", True, BLACK)
                screen.blit(item_name, ([ItemSlotPos, 70]))
            elif item_texture == "hammer.png":
                item_name = font1.render("Hammer", True, BLACK)
                screen.blit(item_name, ([ItemSlotPos - 10, 70]))
            elif item_texture == "banana.png":
                item_name = font1.render("Banana", True, BLACK)
                screen.blit(item_name, ([ItemSlotPos - 10, 70]))
            elif item_texture == "bow.png":
                item_name = font1.render("Bow", True, BLACK)
                screen.blit(item_name, ([ItemSlotPos, 70]))
            elif item_texture == "sword.png":
                item_name = font1.render("Sword", True, BLACK)
                screen.blit(item_name, ([ItemSlotPos - 5, 70]))
            elif item_texture == "ananab.png":
                item_name = font1.render("ananaB", True, WHITE)
                screen.blit(item_name, ([ItemSlotPos - 10, 70]))
            else:
                item_name = font1.render("Unknown Item", True, BLACK)
                screen.blit(item_name, ([ItemSlotPos, 70]))

def item_render(ItemSlotID, ItemID, posx, posy, texture):
    item_id_thing = item_world_id
    SelectedItem = SelectItem
    if True:
        if inv[ItemSlotID] == 0:
            if item_world_id[ItemSlotID] == mapid:
                image_display(screen, item_path + texture, [posx,posy])
                SelectedItem = str(SelectItem)
        elif inv[ItemSlotID] == 1:
            if ItemID == Inv_Slot:
                if not facing == "Right":
                    image_display(screen, item_path + texture, [playerx + 5,playery + 5])
                elif facing == "Right":
                    image_display(screen, item_path + "flipped_" + texture, [playerx + 5,playery + 5])
                SelectedItem = str(ItemSlotID)
            if disable_controls == False:
                if mouse_button_list[2] == True:
                    if not playery + 12 > game_border1:
                        if player_movement[4] == 1:
                            if ItemID == Inv_Slot:
                                posx = playerx + 6
                                posy = playery + 25
                                ItemID = -1
                                inv[ItemSlotID] = 0
                                SelectedItem = "NaN"
                                item_id_thing[ItemSlotID] = mapid
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                    else:
                        playsound(1, environment_audio_path + "wallhit.wav")
    return posx, posy, ItemID, SelectedItem, item_id_thing

def render_slot(slot_id):
    if Inv_Slot == slot_id:
        image_display(screen, inventory_path + "icon_select.png", [minimum_slot + 70 * slot_id, 5])
    elif not Inv_Slot == slot_id:
        image_display(screen, inventory_path + "icon_unselect.png", [minimum_slot + 70 * slot_id, 5])

def render_transparent_slot(slot_id):
    if Inv_Slot == slot_id:
        image_display(screen, inventory_path + transparent_prefix + "icon_select.png", [minimum_slot + 70 * slot_id, 5])
    elif not Inv_Slot == slot_id:
        image_display(screen, inventory_path + transparent_prefix + "icon_unselect.png", [minimum_slot + 70 * slot_id, 5])

def create_square(COLOR, xpos, ypos, width, height):
    SQUARE = pygame.draw.rect(screen, COLOR, [xpos, ypos, width, height])
    return SQUARE

def create_tree_hitbox():
    scores = score
    for i in range(amount_of_trees):
        tree_destroyed = trees_destroyed
        inv_tree_destroyed = inv_trees_destroyed
        tree_destroyed[i], scores = create_tree(0, banana_pos, tree_destroyed[i], tree_positions[i][0], tree_positions[i][1])
        inv_tree_destroyed[i], scores = create_tree(1, ananab_pos, inv_tree_destroyed[i], inv_tree_positions[i][0], inv_tree_positions[i][1])
    return tree_destroyed, inv_tree_destroyed, scores

def create_tree(worldID, drop_item_id, tree_status, posx, posy):
    scores = score
    if mapid == worldID:
        if tree_status == 0:
            tree_hitbox = create_wall(posx, posy, 20, 30)
        else:
            tree_hitbox = create_wall(4000, 4000, 20, 30)
        if pygame.Rect.colliderect(detector_square, tree_hitbox):
            if SelectItem == "2":
                tree_status = 1
                drop_item_id[0] = posx + 10
                drop_item_id[1] = posy + 10
                scores = score + 10
                playsound(1, environment_audio_path + "destroy.wav")
    return tree_status, scores

def render_tree(worldID, treestatus, treetype, posx, posy):
    if mapid == worldID:
        if treestatus == 0:
            image_display(screen, environment_path + treetype, [posx, posy])
def create_wall(xpos, ypos, width, height):
    left = create_square(GREEN, xpos - 3, ypos, 3, height)
    right = create_square(GREEN, xpos + width, ypos, 3, height)
    up = create_square(GREEN, xpos, ypos - 3, width, 3)
    down = create_square(GREEN, xpos, ypos + height, width, 3)
    center = create_square(BLACK, xpos, ypos, width, height)
    if pygame.Rect.colliderect(player_square, left):
        player_movement[1] = 0
    if pygame.Rect.colliderect(player_square, right):
        player_movement[0] = 0
    if pygame.Rect.colliderect(player_square, down):
        player_movement[3] = 0
    if pygame.Rect.colliderect(player_square, up):
        player_movement[2] = 0
    if pygame.Rect.colliderect(item_drop_location, center):
        player_movement[4] = 0
    return center
def deal_damage(damage_amount):
    g = health - damage_amount
    if damage_amount > 0:
        playsound(1, environment_audio_path + "hurt.wav")
    elif damage_amount < 0:
        playsound(1, environment_audio_path + "heal.wav")
    return g
def trigger_use():
    scores = score
    bananas_pos = banana_pos
    ananabs_pos = ananab_pos
    item_id_thing = item_world_id
    healths = health
    if facing == "Right":
        sensor_square = create_square(RED, playerx + square_size, playery, square_size, square_size / 2)
    elif facing == "Left":
        sensor_square = create_square(RED, playerx - square_size, playery, square_size, square_size / 2)
    elif facing == "Up":
        sensor_square = create_square(RED, playerx + square_size / 4, playery - square_size, square_size / 2, square_size)
    elif facing == "Down":
        sensor_square = create_square(RED, playerx + square_size / 4, playery + square_size, square_size / 2, square_size)
    else:
        sensor_square = create_square(RED, 5000, 5000, 10, 10)
    if SelectItem == "4":
        bananas_pos = [3000, 3000]
        # ItemID = -1
        inv[4] = 0
        SelectedItem = "NaN"
        item_id_thing[4] = 0
        healths = deal_damage(-2)
        scores = score + 5
        # playsound(1, environment_audio_path + "use.wav")
    if SelectItem == "5":
        ananabs_pos = [3000, 3000]
        #  = -1
        inv[5] = 0
        SelectedItem = "NaN"
        item_id_thing[5] = 1
        healths = deal_damage(2)
        scores = score + 1
        # playsound(1, environment_audio_path + "use.wav")
    return sensor_square, bananas_pos, ananabs_pos, item_world_id, healths, scores


# Music
if enable_music == True:
    playsound(0, song)
    if show_debug == True:
        print("Playing Music")
elif enable_music == False:
    if show_debug == True:
        print("Music playing is disabled")

# The actual Game
while not done:
        clock.tick(fps)
        screen.fill(background_color)
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        inventory_hitbox = pygame.draw.rect(screen, (255,255,255), [70, 5, 360, 60])
        Selected_Slot = 150 + 70 * Inv_Slot
        # Controls
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if disable_controls == False:
                        if player_movement[0] == 1:
                            if not playerx == game_border2:
                                playerx = playerx - speed
                            elif playerx == game_border2:
                                if mapid == 0:
                                    mapid = 2
                                    playerx = game_border1
                                else:
                                    playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Left"
                        moved = True
                if event.key == pygame.K_d:
                    if disable_controls == False:
                        if player_movement[1] == 1:
                            if not playerx == game_border1:
                                playerx = playerx + speed
                            elif playerx == game_border1:
                                if mapid == 2:
                                    mapid = 0
                                    playerx = game_border2
                                else:
                                    playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Right"
                        moved = True
                if event.key == pygame.K_RETURN:
                    if dead == True:
                        done = True
                if event.key == pygame.K_w:
                    if disable_controls == False:
                        if player_movement[3] == 1:
                            if not playery == game_border2:
                                playery = playery - speed
                            elif playery == game_border2:
                                playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Up"
                        moved = True
                if event.key == pygame.K_s:
                    if disable_controls == False:
                        if player_movement[2] == 1:
                            if not playery == game_border1:
                                playery =playery + speed
                            elif playery == game_border1:
                                playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Down"
                        moved = True
                if event.key == pygame.K_LEFT:
                    if disable_controls == False:
                        if player_movement[0] == 1:
                            if not playerx == game_border2:
                                playerx = playerx - speed
                            elif playerx == game_border2:
                                if mapid == 0:
                                    mapid = 2
                                    playerx = game_border1
                                else:
                                    playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Left"
                        moved = True
                if event.key == pygame.K_RIGHT:
                    if disable_controls == False:
                        if player_movement[1] == 1:
                            if not playerx == game_border1:
                                playerx = playerx + speed
                            elif playerx == game_border1:
                                if mapid == 2:
                                    mapid = 0
                                    playerx = game_border2
                                else:
                                    playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Right"
                        moved = True
                if event.key == pygame.K_UP:
                    if disable_controls == False:
                        if player_movement[3] == 1:
                            if not playery == game_border2:
                                playery = playery - speed
                            elif playery == game_border2:
                                playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Up"
                        moved = True
                if event.key == pygame.K_DOWN:
                    if disable_controls == False:
                        if player_movement[2] == 1:
                            if not playery == game_border1:
                                playery =playery + speed
                            elif playery == game_border1:
                                playsound(1, environment_audio_path + "wallhit.wav")
                        else:
                            playsound(1, environment_audio_path + "wallhit.wav")
                        facing = "Down"
                        moved = True
                if event.key == pygame.K_ESCAPE:
                    done = True
                    if show_debug == True:
                        print("Quit")
                if event.key == pygame.K_q:
                    if disable_controls == False:
                        if not Inv_Slot == 0:
                            Inv_Slot = Inv_Slot - 1
                            # SelectItem = "NaN"
                        elif Inv_Slot == 0:
                            Inv_Slot = 4
                            # SelectItem = "NaN"
                # Dimension key thing
                if event.key == pygame.K_r:
                    if disable_controls == False:
                        if not mapid == 1:
                            if enable_music == True:
                                playsound(0, spookie)
                            previous_map = mapid
                            mapid = 1
                        elif mapid == 1:
                            if enable_music == True:
                                playsound(0, song)
                            if entered_2_1 == False:
                                entered_2_1 = True
                            mapid = previous_map
                if event.key == pygame.K_e:
                    if disable_controls == False:
                        if not Inv_Slot == 4:
                            Inv_Slot = Inv_Slot + 1
                            # SelectItem = "NaN"
                        elif Inv_Slot == 4:
                            Inv_Slot = 0
                            # SelectItem = "NaN"
                if event.key == pygame.K_z:
                    if nextdialog3 == True:
                        nextdialog4 = True
                    if nextdialog2 == True:
                        nextdialog3 = True
                    if nextdialog == True:
                        nextdialog2 = True
                    if show_debug == True:
                        print("Entered")
                    nextdialog = True
                if event.key == pygame.K_f:
                    detector_square, banana_pos, ananab_pos, item_world_id, health, score = trigger_use()
                for i in range(10):
                    if event.key == eval("pygame.K_" + str(i)):
                        if disable_controls == False:
                            if i > INV_MIN:
                                if i - 2 < INV_MAX:
                                    Inv_Slot = i - 1
                                # SelectItem = "NaN"
            if event.type == pygame.QUIT:
                done = True
                if show_debug == True:
                    print("Quit")

        player_movement = [1, 1, 1, 1, player_movement[4]]

        # Mouse Related info
        cursor_pos = pygame.mouse.get_pos()
        cursory = cursor_pos[1] - 5
        cursorx = cursor_pos[0] - 5
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)

        # Hitbox info
        cursor_square = pygame.draw.rect(screen, block_color, [cursorx, cursory, square_size,square_size])
        player_square = pygame.draw.rect(screen, block_color, [playerx,playery,square_size,square_size])
        item_drop_location = pygame.draw.rect(screen, GRAY, [playerx + 6,playery + 25,5,5])

        trees_destroyed, inv_tree_destroyed, score = create_tree_hitbox()
        # inv_tree2_destroyed = create_tree(1, ananab_pos, inv_tree2_destroyed, inv_tree2[0], inv_tree2[1])

        if mapid == 0:
            scientist_square = pygame.draw.rect(screen, block_color, [info_pos[0] - 3,info_pos[1] - 3,square_size + 6,square_size + 6])
        else:
            scientist_square = offscreen

        # Item Managment
        hammer_slot[0], hammer_slot[1] = item_detector(0, "item1", hammer_slot[0], hammer_slot[1], hammer_pos[0], hammer_pos[1])
        sword_slot[0], sword_slot[1] = item_detector(1, "item2", sword_slot[0], sword_slot[1], sword_pos[0], sword_pos[1])
        axe_slot[0], axe_slot[1] = item_detector(2, "item3", axe_slot[0], axe_slot[1], axe_pos[0], axe_pos[1])
        bow_slot[0], bow_slot[1] = item_detector(3, "item4", bow_slot[0], bow_slot[1], bow_pos[0], bow_pos[1])
        banana_slot[0], banana_slot[1] = item_detector(4, "item5", banana_slot[0], banana_slot[1], banana_pos[0], banana_pos[1])
        ananab_slot[0], ananab_slot[1] = item_detector(5, "item6", ananab_slot[0], ananab_slot[1], ananab_pos[0], ananab_pos[1])
        SelectItem = "NaN"
        # Background and players
        if disable_background == False:
            if mapid == 0:
                image_display(screen, environment_path + "background.png", [0,0])
            elif mapid == 2:
                image_display(screen, environment_path + "background.png", [0,0])
            elif mapid == 1:
                image_display(screen, environment_path + "background0.png", [0,0])
        #
        if facing == "Left":
            image_display(screen, characters_path + "Player/playerflipped.png", [playerx,playery])
        elif facing == "Right":
            image_display(screen, characters_path + "Player/player.png", [playerx,playery])
        elif facing == "Up":
            image_display(screen, characters_path + "Player/playerup.png", [playerx,playery])
        elif facing == "Down":
            image_display(screen, characters_path + "Player/playerdown.png", [playerx,playery])
        else:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: PLAYER_ROTATION_INVALID" + style.RESET)
            done = True
        if mapid == 0:
            if scientist_leaving == True:
                image_display(screen, characters_path + "Scientist/scientist.png", [info_pos[0],info_pos[1]])
            else:
                if playerx > info_pos[0]:
                    image_display(screen, characters_path + "Scientist/scientist.png", [info_pos[0],info_pos[1]])
                elif playerx < info_pos[0]:
                    image_display(screen, characters_path + "Scientist/scientist_flipped.png", [info_pos[0],info_pos[1]])
                elif playerx == info_pos[0]:
                    if playery > info_pos[1]:
                        image_display(screen, characters_path + "Scientist/scientist_down.png", [info_pos[0],info_pos[1]])
                    elif playery < info_pos[1]:
                        image_display(screen, characters_path + "Scientist/scientist_up.png", [info_pos[0],info_pos[1]])

        # Trees
        for i in range(amount_of_trees):
            tree_destroyed = trees_destroyed
            inv_tree_destroyed = inv_trees_destroyed
            render_tree(0, tree_destroyed[i], "tree.png", tree_positions[i][0], tree_positions[i][1])
            render_tree(1, inv_tree_destroyed[i], "tree_inverted.png", inv_tree_positions[i][0], inv_tree_positions[i][1])

        # Health Bar
        if health > max_health:
            health = max_health
        poison_duration, health = poison_effect()
        health_tick = health_bar()
        if health < 1:
            dead = True
            disable_controls = True

        # Inventory Stuff
        hammer_pos[0], hammer_pos[1], hammer_slot[0], SelectItem, item_world_id = item_render(0, hammer_slot[0], hammer_pos[0], hammer_pos[1], "hammer.png")
        sword_pos[0], sword_pos[1], sword_slot[0], SelectItem, item_world_id = item_render(1, sword_slot[0], sword_pos[0], sword_pos[1], "sword.png")
        axe_pos[0], axe_pos[1], axe_slot[0], SelectItem, item_world_id = item_render(2, axe_slot[0], axe_pos[0], axe_pos[1], "axe.png")
        bow_pos[0], bow_pos[1], bow_slot[0], SelectItem, item_world_id = item_render(3, bow_slot[0], bow_pos[0], bow_pos[1], "bow.png")
        banana_pos[0], banana_pos[1], banana_slot[0], SelectItem, item_world_id = item_render(4, banana_slot[0], banana_pos[0], banana_pos[1], "banana.png")
        ananab_pos[0], ananab_pos[1], ananab_slot[0], SelectItem, item_world_id = item_render(5, ananab_slot[0], ananab_pos[0], ananab_pos[1], "ananab.png")
        if pygame.Rect.colliderect(inventory_hitbox, player_square) == True:
            render_transparent_slot(0)
            render_transparent_slot(1)
            render_transparent_slot(2)
            render_transparent_slot(3)
            render_transparent_slot(4)
        elif pygame.Rect.colliderect(inventory_hitbox, player_square) == False:
            render_slot(0)
            render_slot(1)
            render_slot(2)
            render_slot(3)
            render_slot(4)

        render_item_inv("hammer.png", 0, hammer_slot[0], hammer_slot[1])
        render_item_inv("sword.png", 1, sword_slot[0], sword_slot[1])
        render_item_inv("axe.png", 2, axe_slot[0], axe_slot[1])
        render_item_inv("bow.png", 3, bow_slot[0], bow_slot[1])
        render_item_inv("banana.png", 4, banana_slot[0], banana_slot[1])
        render_item_inv("ananab.png", 5, ananab_slot[0], ananab_slot[1])

        # Deatch Screen
        if dead == True:
            create_square(GRAY, 15, 15, 470, 470)
            deadfont = pygame.font.SysFont('A totally real font', 50)
            deadfont2 = pygame.font.SysFont('A totally real font', 30)
            death_message = deadfont.render("Game Over!", True, RED)
            screen.blit(death_message, (150, 60))
            death_notice = deadfont2.render("Press enter to exit", True, RED)
            screen.blit(death_notice, (165, 350))
            score_font = pygame.font.SysFont('A totally real font', 25)
            score_death_message = score_font.render("Score: " + str(score), True, BLACK)
            screen.blit(score_death_message, (215, 225))
            nextdialog = True
            nextdialog2 = True
            nextdialog3 = True
            nextdialog4 = True

        # Dialogs
        if pygame.Rect.colliderect(player_square, scientist_square) == 1:
            if nextdialog4 == False:
                moved = False
            if SelectItem == "NaN":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "Hello User!")
                    create_notice(200, 200)
                if nextdialog == True:
                    disable_controls = False
                    nextdialog2 = True
                    nextdialog3 = True
                    nextdialog4 = True
            if SelectItem == "1":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "Why are you holding a sword?")
                    create_notice(200, 200)
                if nextdialog == True:
                    disable_controls = False
                    nextdialog2 = True
                    nextdialog3 = True
                    nextdialog4 = True
            if SelectItem == "0":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "Unfortunatly, you can't do anything with hammers yet.")
                    create_notice(200, 200)
                if nextdialog == True:
                    disable_controls = False
                    nextdialog2 = True
                    nextdialog3 = True
                    nextdialog4 = True
            if SelectItem == "3":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "I see you have found a bow")
                    create_notice(200, 200)
                if nextdialog == True:
                    disable_controls = False
                    nextdialog2 = True
                    nextdialog3 = True
                    nextdialog4 = True
            if SelectItem == "2":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "You can use that toothbr- I mean axe to cut down trees")
                    create_notice(200, 200)
                if nextdialog == True:
                    disable_controls = False
            if SelectItem == "4":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "Is... is.. that.. A BANANA!?")
                if nextdialog == True:
                    scientist_leaving = scientist_leaving = True
                    createdialog("Scientist", "AAAAAHHHH!")
                    disable_controls = False
                    create_notice(info_pos[0], info_pos[1])
            if SelectItem == "5":
                if nextdialog == False:
                    disable_controls = True
                    createdialog("Scientist", "?!ANANAB A ..taht ..si ...sI")
                if nextdialog == True:
                    scientist_leaving = scientist_leaving = True
                    createdialog("Scientist", "!HHHHAAAAA")
                    disable_controls = False
                    create_notice(info_pos[0], info_pos[1])
            if show_debug == True:
                print("Dialog Opened")
            #
        if scientist_leaving == True:
            info_pos[0] = info_pos[0] + 5

        if nextdialog4 == True:
            disable_controls = False
        if nextdialog == True:
            if moved == True:
                nextdialog = False
                nextdialog2 = False
                nextdialog3 = False
                nextdialog4 = False

        # Debugging stuff
        if show_debug == True:
            print("Inventory Data")
            print("Inv_Slot: " + str(Inv_Slot))
            print("Hammer Slot: " + str(hammer_slot[0]))
            print("Sword Slot: " + str(sword_slot[0]))
            print("Axe Slot: " + str(axe_slot[0]))
            print("Held Item: " + SelectItem)
            print()
            print("Tree Data")
            # print("Trees Destroyed: " + str(trees_destroyed))
            # print("Tree Positions: " + str(tree_positions))
            print("Banana: " + str(True))
            print()
            print("Player Data")
            print("Controls Status: " + str(disable_controls))
            print("Player Rotation: " + facing)
            print("Player Movement: " + str(player_movement))
            print()
            print("Dialog Internals")
            print(nextdialog)
            print(nextdialog2)
            print(nextdialog3)
            print(nextdialog4)
            print()
            print("World Data")
            print("World ID: " + str(mapid))
            print("Item World ID: " + str(item_world_id))
            print()

        # Update display
        pygame.display.update()
        pygame.display.flip()

        # Disable controls if player is dead
        if dead == True:
            disable_controls = True

        # Reset variables for next tick
        detector_square = offscreen
        player_movement = [player_movement[0],player_movement[1],player_movement[2],player_movement[3],1]

        # Game Variable Checker
        if playerx > game_border1:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: PLAYER_POS_OUT_OF_RANGE" + style.RESET)
            done = True
        elif playery > game_border1:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: PLAYER_POS_OUT_OF_RANGE" + style.RESET)
            done = True
        if playerx < game_border2:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: PLAYER_POS_OUT_OF_RANGE" + style.RESET)
            done = True
        elif playery < game_border2:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: PLAYER_POS_OUT_OF_RANGE" + style.RESET)
            done = True
        if Inv_Slot < INV_MIN:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: INVALID_INV_SLOT" + style.RESET)
            done = True
        if Inv_Slot > INV_MAX:
            print(fore.WHITE + back.RED + style.BOLD + "ERROR: INVALID_INV_SLOT" + style.RESET)
            done = True
pygame.quit()
exit()
