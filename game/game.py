# Script Modules
import os # Disabling Pygame support prompt
import platform # Used to check if system is compatible with the script
import sys, pathlib # Used for importing from Language folder
import time # For game ticking
import math, random # For generating random numbers
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame # Used to make graphical windows
from pygame.locals import * # Import some pygame utils
pygame.init()
from shared import * # Import game variables
current_path = pathlib.Path().parent.absolute()
sys.path.insert(1, str(current_path) + '/Language')
from lang import * # Import language text file
from colored import fore, back, style # For Colorful text
pygame.mixer.init() # Music to my ears

# The Credits
print(fore.BLUE)
print("Program by Trains77")
print()
print("Artwork by Trains77")
print()
#print("Background Music: https://www.FesliyanStudios.com and")
#print("                  https://freemusicarchive.org/music/defrini")
#print()
print("Made with Atom Editor")
print()
print("Utilizes Pygame")
print()
print("AnotherGame " + version)
print(style.RESET)

# System Checker
if not platform.system() == system_recommends:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this program" + style.RESET)
if enable_program == True:
    done = False
elif enable_program == False:
    print("The program has been disabled in shared.py")
    print()
    print(fore.WHITE + back.RED + style.BOLD + "ERROR: GAME_DISABLED" + style.RESET)
    done = True

# Functions
def createdialog(speaker, text):
    dialog_box = pygame.draw.rect(screen, dialog_color, [10,350,480,140])
    img1 = font1.render(speaker + ":", True, BLACK)
    img2 = font1.render(text, True, BLACK)
    img3 = font1.render(dialog_continue, True, BLACK)
    screen.blit(img1, (15, 360))
    screen.blit(img2, (30, 390))
    screen.blit(img3, (355, 470))
def poison_effect():
    last_damages = last_damage
    healths = health
    poison = poison_duration
    if health_tick == 19:
        if poison > 0:
            healths, last_damages = deal_damage(1, "poison")
            poison = poison - 1
    return poison, healths, last_damages
def create_notice(posx, posy):
    img4 = pygame.image.load(characters_path + "speaking.png")
    screen.blit(img4, [posx, posy - 20])

def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)

def playsound(channel,audiofile):
    if enable_audio == True:
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
    health_txt = font1.render(game_healthbar + str(health) + "/" + str(max_health), True, BLACK)
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
                    if enable_debug == 1:
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
                item_name = font1.render(item_axe, True, BLACK)
                screen.blit(item_name, ([ItemSlotPos, 70]))
            elif item_texture == "hammer.png":
                item_name = font1.render(item_hammer, True, BLACK)
                screen.blit(item_name, ([ItemSlotPos - 10, 70]))
            elif item_texture == "banana.png":
                item_name = font1.render(item_banana, True, BLACK)
                screen.blit(item_name, ([ItemSlotPos - 10, 70]))
            elif item_texture == "bow.png":
                item_name = font1.render(item_bow, True, BLACK)
                screen.blit(item_name, ([ItemSlotPos, 70]))
            elif item_texture == "sword.png":
                item_name = font1.render(item_sword, True, BLACK)
                screen.blit(item_name, ([ItemSlotPos - 5, 70]))
            elif item_texture == "ananab.png":
                item_name = font1.render(item_ananab, True, WHITE)
                screen.blit(item_name, ([ItemSlotPos - 10, 70]))
            else:
                item_name = font1.render(item_unknown, True, BLACK)
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
                    image_display(screen, item_path + texture, [playerx + 5,playery - jump + 5])
                elif facing == "Right":
                    image_display(screen, item_path + "flipped_" + texture, [playerx + 5,playery - jump + 5])
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
        tree_destroyed[i], scores = create_tree(0, item_pos[4], tree_destroyed[i], tree_positions[i][0], tree_positions[i][1])
        inv_tree_destroyed[i], scores = create_tree(1, item_pos[5], inv_tree_destroyed[i], inv_tree_positions[i][0], inv_tree_positions[i][1])
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
def deal_damage(damage_amount, damage_type):
    g = health
    last_damages = last_damage
    if dead == False:
        g = health - damage_amount
        if damage_amount > 0:
            if damage_type == "poison":
                last_damages = "poison"
            elif damage_type == "arrow":
                last_damages = "arrow"
            elif damage_type == "melee":
                last_damages = "melee"
            elif damage_type == "debug":
                last_damages = "debug"
            elif damage_type == "banana":
                last_damages = "banana"
            elif damage_type == "generic":
                last_damages = "generic"
            else:
                last_damages = "generic"
            playsound(1, environment_audio_path + "hurt.wav")
        elif damage_amount < 0:
            playsound(1, environment_audio_path + "heal.wav")
    return g, last_damages
def trigger_use():
    last_damages = last_damage
    arrow_positions = arrows_positions
    scores = score
    bananas_pos = item_pos[4]
    ananabs_pos = item_pos[5]
    arrows_amount = arrow_amount
    item_id_thing = item_world_id
    healths = health
    if SelectItem == "3":
        playsound(1, environment_audio_path + "shoot.wav")
        if facing == "Right":
            arrow_positions.append([playerx + 23, playery + 5, facing])
            arrows_amount = arrows_amount + 1
        elif facing == "Left":
            arrow_positions.append([playerx - 7, playery + 5, facing])
            arrows_amount = arrows_amount + 1
        elif facing == "Down":
            arrow_positions.append([playerx + 9, playery + 20, facing])
            arrows_amount = arrows_amount + 1
        elif facing == "Up":
            arrow_positions.append([playerx + 9, playery - 7, facing])
            arrows_amount = arrows_amount + 1
    if facing == "Right":
        sensor_square = create_square(RED, playerx + square_size, playery - jump, square_size, square_size / 2)
    elif facing == "Left":
        sensor_square = create_square(RED, playerx - square_size, playery - jump, square_size, square_size / 2)
    elif facing == "Up":
        sensor_square = create_square(RED, playerx + square_size / 4, playery - jump - square_size, square_size / 2, square_size)
    elif facing == "Down":
        sensor_square = create_square(RED, playerx + square_size / 4, playery - jump + square_size, square_size / 2, square_size)
    else:
        sensor_square = create_square(RED, 5000, 5000, 10, 10)
    if SelectItem == "4":
        bananas_pos = [3000, 3000]
        inv[4] = 0
        SelectedItem = "NaN"
        item_id_thing[4] = 0
        healths, last_damages = deal_damage(-2, "banana")
        scores = score + 5
    if SelectItem == "5":
        ananabs_pos = [3000, 3000]
        #  = -1
        inv[5] = 0
        SelectedItem = "NaN"
        item_id_thing[5] = 1
        healths, last_damages = deal_damage(2, "banana")
        scores = score + 1
    return sensor_square, bananas_pos, ananabs_pos, item_world_id, healths, scores, arrow_positions, arrows_amount, last_damages
def render_enemy(map,enemyID,speeds,type):
    healths = health
    scores = score
    enemy_statuss = enemy_status
    enemyPosition = enemyPositions
    poisons = poison_duration
    # Enemy Attack
    if map == mapid:
        if enemy_statuss[enemyID][0] == 1:
            if pygame.Rect.colliderect(player_square, enemy_squares[enemyID]) == 1:
                if type == 0:
                    if health_tick == 19:
                        healths, last_damage = deal_damage(1, "melee")
                elif type == 1:
                    if health_tick == 19:
                        poisons = poisons + 1
                    elif health_tick == 10:
                        poisons = poisons + 1
                    elif health_tick == 5:
                        poisons = poisons + 1
                    elif health_tick == 15:
                        poisons = poisons + 1
    # Kill enemy
    if pygame.Rect.colliderect(detector_square, enemy_squares[enemyID]) == 1:
        if SelectItem == "1":
            enemy_statuss[enemyID][0] = 0
            scores = scores + 10
    elif enemy_statuss[enemyID][0] == 0:
        enemyPosition[enemyID][0] = 900
    # Enemy Movements
    if enemy_statuss[enemyID][0] == 1:
        if mapid == map:
            if type == 0:
                if playerx > enemyPositions[enemyID][0]:
                    image_display(screen, characters_path + "Enemy/enemy.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    enemyPosition[enemyID][0] = enemyPosition[enemyID][0] + speeds
                elif playerx < enemyPosition[enemyID][0]:
                    image_display(screen, characters_path + "Enemy/enemy_flipped.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    enemyPosition[enemyID][0] = enemyPosition[enemyID][0] - speeds
                elif playery - jump > enemyPosition[enemyID][1]:
                    image_display(screen, characters_path + "Enemy/enemy_down.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    enemyPosition[enemyID][1] = enemyPosition[enemyID][1] + speeds
                elif playery - jump < enemyPosition[enemyID][1]:
                    image_display(screen, characters_path + "Enemy/enemy_up.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    enemyPosition[enemyID][1] = enemyPosition[enemyID][1] - speeds
            elif type == 1:
                if playerx == enemyPosition[enemyID][0]:
                    if playery < enemyPosition[enemyID][1]:
                        image_display(screen, characters_path + "Enemy/poison_enemy_up.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    else:
                        image_display(screen, characters_path + "Enemy/poison_enemy_down.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                if playerx > enemyPositions[enemyID][0]:
                    image_display(screen, characters_path + "Enemy/poison_enemy.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    enemyPosition[enemyID][0] = enemyPosition[enemyID][0] + speeds
                elif playerx < enemyPosition[enemyID][0]:
                    image_display(screen, characters_path + "Enemy/poison_enemy_flipped.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
                    enemyPosition[enemyID][0] = enemyPosition[enemyID][0] - speeds
                if playery - jump > enemyPosition[enemyID][1]:
                    enemyPosition[enemyID][1] = enemyPosition[enemyID][1] + speeds
                elif playery - jump < enemyPosition[enemyID][1]:
                    enemyPosition[enemyID][1] = enemyPosition[enemyID][1] - speeds
                else:
                    if playerx == enemyPositions[enemyID][0]:
                        image_display(screen, characters_path + "Enemy/poison_enemy_down.png", [enemyPosition[enemyID][0],enemyPosition[enemyID][1]])
    return enemyPosition, healths, enemy_statuss, scores, poisons
detector_square = create_square(RED, 5000, 5000, 10, 10)
def arrow_proc():
    enemy_statuss = enemy_status
    healths = health
    arrow_positions = arrows_positions
    arrows_amount = arrow_amount
    if not arrows_amount <= 0:
        for i in range(arrows_amount):
            g = i
            #
            if len(arrow_positions) > i:
                arrow = pygame.draw.rect(screen, DARK_GRAY, [arrow_positions[i][0], arrow_positions[i][1], 5, 5])
                if pygame.Rect.colliderect(arrow, player_square) == True:
                    healths, last_damage = deal_damage(1, "arrow")
                    del arrow_positions[g]
                    arrows_amount = arrows_amount - 1
                elif arrow_positions[i][1] >= 500:
                    del arrow_positions[g]
                    arrows_amount = arrows_amount - 1
                elif arrow_positions[i][1] <= 0:
                    del arrow_positions[g]
                    arrows_amount = arrows_amount - 1
                elif arrow_positions[i][0] >= 500:
                    del arrow_positions[g]
                    arrows_amount = arrows_amount - 1
                elif arrow_positions[i][0] <= 0:
                    del arrow_positions[g]
                    arrows_amount = arrows_amount - 1
                else:
                    if arrow_positions[i][2] == "Right":
                        arrow_positions[i][0] = arrow_positions[i][0] + 10
                    elif arrow_positions[i][2] == "Left":
                        arrow_positions[i][0] = arrow_positions[i][0] - 10
                    elif arrow_positions[i][2] == "Up":
                        arrow_positions[i][1] = arrow_positions[i][1] - 10
                    elif arrow_positions[i][2] == "Down":
                        arrow_positions[i][1] = arrow_positions[i][1] + 10
                    for i in range(enemy_count):
                        if pygame.Rect.colliderect(arrow,enemy_squares[i]):
                            enemy_status[i][0] = 0
                            del arrow_positions[g]
                            arrows_amount = arrows_amount - 1
    return healths, enemy_statuss, arrow_positions, arrows_amount
# Play game music
if enable_music == True:
    playsound(0, song)

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
                    if enable_debug == True:
                        print("Quit")
                if event.key == pygame.K_q:
                    if disable_controls == False:
                        if not Inv_Slot == 0:
                            Inv_Slot = Inv_Slot - 1
                        elif Inv_Slot == 0:
                            Inv_Slot = 4
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
                            mapid = 0
                if event.key == pygame.K_e:
                    if disable_controls == False:
                        if not Inv_Slot == 4:
                            Inv_Slot = Inv_Slot + 1
                        elif Inv_Slot == 4:
                            Inv_Slot = 0
                if event.key == pygame.K_SPACE:
                    if disable_controls == False:
                        if jump == 0:
                            velocityY = 10
                            playsound(1, environment_audio_path + "jump.wav")
                if event.key == pygame.K_k:
                    if disable_controls == False:
                        if enable_debug == True:
                            health, last_damage = deal_damage(999999, "debug")
                if event.key == pygame.K_z:
                    if nextdialog3 == True:
                        nextdialog4 = True
                    if nextdialog2 == True:
                        nextdialog3 = True
                    if nextdialog == True:
                        nextdialog2 = True
                    if enable_debug == True:
                        print(debug_enter)
                    nextdialog = True
                if event.key == pygame.K_f:
                    detector_square, item_pos[4], item_pos[5], item_world_id, health, score, arrows_positions, arrow_amount, last_damage = trigger_use()
                for i in range(10):
                    if event.key == eval("pygame.K_" + str(i)):
                        if disable_controls == False:
                            if i > INV_MIN:
                                if i - 2 < INV_MAX:
                                    Inv_Slot = i - 1
            if event.type == pygame.QUIT:
                done = True
                if enable_debug == True:
                    print("Quit")
        # Player jumping logic
        player_movement = [1, 1, 1, 1, player_movement[4]]
        if velocityY > 0:
            if jump < velocityY:
                jump = jump + 2
            elif velocityY == jump:
                velocityY = velocityY - 2
                jump = jump - 2

        # Mouse Related info
        cursor_pos = pygame.mouse.get_pos()
        cursory = cursor_pos[1] - 5
        cursorx = cursor_pos[0] - 5
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)

        # Hitbox info
        cursor_square = pygame.draw.rect(screen, block_color, [cursorx, cursory, square_size,square_size])
        player_square = pygame.draw.rect(screen, block_color, [playerx,playery - jump,square_size,square_size])
        item_drop_location = pygame.draw.rect(screen, GRAY, [playerx + 6,playery + 25,5,5])
        trees_destroyed, inv_tree_destroyed, score = create_tree_hitbox()
        enemy_squares = enemy_squares
        if mapid == 0:
            scientist_square = pygame.draw.rect(screen, block_color, [info_pos[0] - 3,info_pos[1] - 3,square_size + 6,square_size + 6])
        else:
            scientist_square = offscreen
        for i in range(enemy_count):
            enemy_squares.append(pygame.draw.rect(screen, RED, [enemyPositions[i][0], enemyPositions[i][1],square_size,square_size]))
        # Item Managment
        hammer_slot[0], hammer_slot[1] = item_detector(0, "item1", hammer_slot[0], hammer_slot[1], item_pos[0][0], item_pos[0][1])
        sword_slot[0], sword_slot[1] = item_detector(1, "item2", sword_slot[0], sword_slot[1], item_pos[1][0], item_pos[1][1])
        axe_slot[0], axe_slot[1] = item_detector(2, "item3", axe_slot[0], axe_slot[1], item_pos[2][0], item_pos[2][1])
        bow_slot[0], bow_slot[1] = item_detector(3, "item4", bow_slot[0], bow_slot[1], item_pos[3][0], item_pos[3][1])
        banana_slot[0], banana_slot[1] = item_detector(4, "item5", banana_slot[0], banana_slot[1], item_pos[4][0], item_pos[4][1])
        ananab_slot[0], ananab_slot[1] = item_detector(5, "item6", ananab_slot[0], ananab_slot[1], item_pos[5][0], item_pos[5][1])

        # Background and players
        if disable_background == False:
            if mapid == 0:
                image_display(screen, environment_path + "background.png", [0,0])
            elif mapid == 2:
                image_display(screen, environment_path + "background.png", [0,0])
            elif mapid == 1:
                image_display(screen, environment_path + "background0.png", [0,0])
        #
        if jump > 0:
            if facing == "Left":
                image_display(screen, characters_path + "shadow_flipped.png", [playerx,playery + 2])
            elif facing == "Up":
                image_display(screen, characters_path + "shadow_flipped.png", [playerx,playery + 2])
            else:
                image_display(screen, characters_path + "shadow.png", [playerx,playery + 2])
        if dead == False:
            if facing == "Left":
                image_display(screen, characters_path + "Player/playerflipped.png", [playerx,playery - jump])
            elif facing == "Right":
                image_display(screen, characters_path + "Player/player.png", [playerx,playery - jump])
            elif facing == "Up":
                image_display(screen, characters_path + "Player/playerup.png", [playerx,playery - jump])
            elif facing == "Down":
                image_display(screen, characters_path + "Player/playerdown.png", [playerx,playery - jump])
            else:
                print(fore.WHITE + back.RED + style.BOLD + error_error + error_rotation + style.RESET)
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
        enemyPositions, health, enemy_status, score, poison_duration = render_enemy(2,0,2,0)
        enemypositions, health, enemy_status, score, poison_duration = render_enemy(2,1,1,1)
        SelectItem = "NaN"

        # Arrows
        health, enemy_status, arrows_positions, arrow_amount = arrow_proc()

        # Trees
        for i in range(amount_of_trees):
            tree_destroyed = trees_destroyed
            inv_tree_destroyed = inv_trees_destroyed
            render_tree(0, tree_destroyed[i], "tree.png", tree_positions[i][0], tree_positions[i][1])
            render_tree(1, inv_tree_destroyed[i], "tree_inverted.png", inv_tree_positions[i][0], inv_tree_positions[i][1])

        # Health Bar
        if health > max_health:
            health = max_health
        poison_duration, health, last_damage = poison_effect()
        health_tick = health_bar()
        if health < 1:
            dead = True
            disable_controls = True

        # Controls
        if show_controls == True:
            if disable_controls == False:
                Control_Font = pygame.font.SysFont('A totally real font', 15)
                Control_Text1 = Control_Font.render(control_wasd, True, BLACK)
                screen.blit(Control_Text1, (428, 430))
                Control_Font = pygame.font.SysFont('A totally real font', 15)
                Control_Text1 = Control_Font.render(control_spacebar, True, BLACK)
                screen.blit(Control_Text1, (415, 440))
                Control_Text2 = Control_Font.render(control_esc, True, BLACK)
                screen.blit(Control_Text2, (445, 420))
                Control_Text1 = Control_Font.render(control_f_key, True, BLACK)
                screen.blit(Control_Text1, (430, 450))
                Control_Text1 = Control_Font.render(control_right_click, True, BLACK)
                screen.blit(Control_Text1, (410, 470))
                Control_Text1 = Control_Font.render(control_q_e_key, True, BLACK)
                screen.blit(Control_Text1, (370, 480))
                Control_Text1 = Control_Font.render(control_r_key, True, BLACK)
                screen.blit(Control_Text1, (425, 460))
                if enable_debug == True:
                    Control_Text1 = Control_Font.render(control_debug_k_key, True, BLACK)
                    screen.blit(Control_Text1, (425, 490))
        # Inventory Stuff
        item_pos[0][0], item_pos[0][1], hammer_slot[0], SelectItem, item_world_id = item_render(0, hammer_slot[0], item_pos[0][0], item_pos[0][1], "hammer.png")
        item_pos[1][0], item_pos[1][1], sword_slot[0], SelectItem, item_world_id = item_render(1, sword_slot[0], item_pos[1][0], item_pos[1][1], "sword.png")
        item_pos[2][0], item_pos[2][1], axe_slot[0], SelectItem, item_world_id = item_render(2, axe_slot[0], item_pos[2][0], item_pos[2][1], "axe.png")
        item_pos[3][0], item_pos[3][1], bow_slot[0], SelectItem, item_world_id = item_render(3, bow_slot[0], item_pos[3][0], item_pos[3][1], "bow.png")
        item_pos[4][0], item_pos[4][1], banana_slot[0], SelectItem, item_world_id = item_render(4, banana_slot[0], item_pos[4][0], item_pos[4][1], "banana.png")
        item_pos[5][0], item_pos[5][1], ananab_slot[0], SelectItem, item_world_id = item_render(5, ananab_slot[0], item_pos[5][0], item_pos[5][1], "ananab.png")
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

        # Death Screen
        if dead == True:
            create_square(GRAY, 15, 15, 470, 470)
            deadfont = pygame.font.SysFont('A totally real font', 50)
            deadfont2 = pygame.font.SysFont('A totally real font', 30)
            death_message = deadfont.render(death_game_end, True, RED)
            screen.blit(death_message, (150, 60))
            death_notice = deadfont2.render(death_exit, True, RED)
            screen.blit(death_notice, (165, 350))
            score_font = pygame.font.SysFont('A totally real font', 25)
            score_death_message = score_font.render(game_score + str(score), True, BLACK)
            screen.blit(score_death_message, (215, 225))
            nextdialog = True
            nextdialog2 = True
            nextdialog3 = True
            nextdialog4 = True
            if last_damage == "generic":
                e = death_generic
            elif last_damage == "poison":
                e = death_poison
            elif last_damage == "debug":
                e = death_debug
            elif last_damage == "melee":
                e = death_melee
            elif last_dmage == "arrow":
                e = death_arrow
            elif last_damage == "banana":
                e = death_banana
            else:
                e = death_test
            death_reason = score_font.render(e[0], True, BLACK)
            screen.blit(death_reason, e[1])
        # Dialogs
        if pygame.Rect.colliderect(player_square, scientist_square) == 1:
            if jump == 0:
                if nextdialog4 == False:
                    moved = False
                if SelectItem == "NaN":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_generic)
                        create_notice(200, 200)
                    if nextdialog == True:
                        disable_controls = False
                        nextdialog2 = True
                        nextdialog3 = True
                        nextdialog4 = True
                if SelectItem == "1":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_sword)
                        create_notice(200, 200)
                    if nextdialog == True:
                        disable_controls = False
                        nextdialog2 = True
                        nextdialog3 = True
                        nextdialog4 = True
                if SelectItem == "0":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_hammer)
                        create_notice(200, 200)
                    if nextdialog == True:
                        disable_controls = False
                        nextdialog2 = True
                        nextdialog3 = True
                        nextdialog4 = True
                if SelectItem == "3":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_bow)
                        create_notice(200, 200)
                    if nextdialog == True:
                        disable_controls = False
                        nextdialog2 = True
                        nextdialog3 = True
                        nextdialog4 = True
                if SelectItem == "2":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_axe)
                        create_notice(200, 200)
                    if nextdialog == True:
                        disable_controls = False
                if SelectItem == "4":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_banana_1)
                    if nextdialog == True:
                        scientist_leaving = scientist_leaving = True
                        createdialog(scientist_name, scientist_dialog_banana_2)
                        disable_controls = False
                        create_notice(info_pos[0], info_pos[1])
                if SelectItem == "5":
                    if nextdialog == False:
                        disable_controls = True
                        createdialog(scientist_name, scientist_dialog_invbanana_1)
                    if nextdialog == True:
                        scientist_leaving = scientist_leaving = True
                        createdialog(scientist_name, scientist_dialog_invbanana_2)
                        disable_controls = False
                        create_notice(info_pos[0], info_pos[1])
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
        if enable_debug == True:
            print(debug_inventory_text)
            print(debug_inventory_slot + str(Inv_Slot))
            print(debug_inventory_select + SelectItem)
            print()
            print(debug_player_text)
            print(debug_player_controls + str(disable_controls))
            print(debug_player_rotation + facing)
            print(debug_player_movement + str(player_movement))
            print(debug_player_damaged + last_damage)
            print()
            print(debug_dialog_text)
            print(nextdialog)
            print(nextdialog2)
            print(nextdialog3)
            print(nextdialog4)
            print()
            print(debug_world_text)
            print(debug_world_mapid + str(mapid))
            print(debug_world_itemid + str(item_world_id))
            print(debug_world_tree_destroyed + str(trees_destroyed))
            print(debug_world_invtree_destroyed + str(inv_trees_destroyed))
            print(debug_world_tree_pos + str(tree_positions))
            print(debug_world_invtree_pos + str(inv_tree_positions))
            print(debug_world_arrow + str(arrows_positions))
            print(debug_world_arrow_amount + str(arrow_amount))
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
        enemy_squares = []

        # Checks if variables are valid
        if playerx > game_border1:
            print(fore.WHITE + back.RED + style.BOLD + error_error +  + style.RESET)
            done = True
        elif playery > game_border1:
            print(fore.WHITE + back.RED + style.BOLD + error_error + error_pos + style.RESET)
            done = True
        if playerx < game_border2:
            print(fore.WHITE + back.RED + style.BOLD + error_error + error_pos + style.RESET)
            done = True
        elif playery < game_border2:
            print(fore.WHITE + back.RED + style.BOLD + error_error + error_pos + style.RESET)
            done = True
        if Inv_Slot < INV_MIN:
            print(fore.WHITE + back.RED + style.BOLD + error_error + error_inv + style.RESET)
            done = True
        if Inv_Slot > INV_MAX:
            print(fore.WHITE + back.RED + style.BOLD + error_error + error_inv + style.RESET)
            done = True
pygame.quit()
exit()
