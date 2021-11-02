# Stuff for variables
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

# Debugging settings
disable_background = False # Set whether the game loads the background file
player_color = (0, 0, 0) # The color of the player hitbox
block_color = (0, 0, 0) # Block Color
info_color = (150, 150, 150) # Info square color
dialog_color = (255, 255, 255) # Dialog box color
background_color = (128, 0, 128) # The background color of the game
show_debug = False # Enable debugging messages
inventory_path = "Textures/slot/" # Where to pull Inventory and gui textures from
item_path = "Textures/items/" # Where to pull item textures from
environment_audio_path = "Audio/Environment/" # Where to pull environment audio from
environment_path = "Textures/Environment/" # Where to pull environmental textures from
characters_path = "Textures/Characters/" # Where to pull character textures from

# Game Settings
enable_os_restrictions = 0 # Whether to enable strict os checking
credits = 1 # Whether to display credits at startup
GameName = "Another Python Game" # The name of the game
song = 'Audio/Music/music1.wav' # Path to music file
enable_music = 1 # Whether or not music is enabled
gameIcon = pygame.image.load('Textures/Icons/game.png') # Path to game's window icon
Inv_Slot = 0 # Default inventory slot

# WARNING: Changing these settings will cause issues
enable_os_restrictions = 0 # Whether to enable strict os checking
size = [500, 500] # The size of the screen
square_size = 20 # How big the default hitbox is
game_border1 = 480 # Maximum cordinates player can be
game_border2 = 0 # Minimum cordinates playerr can be
speed = 10 # How fast the player moves
enable_program = True # Enables or Disables the program
item_size = 10 # The size of an item's hitbox
fps = 10 # The FPS of the game
inv = [0, 0, 0, 0] # Inventory list
minimum_slot = 80

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
