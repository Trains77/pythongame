# Stuff for variables
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

# Game Settings
enable_os_restrictions = 0 # Whether to disable usage on non-Linux systems, will be deprecated soon
GameName = "Another Python Game" # The name of the game
song = 'Audio/Music/music1.wav' # Path to music file
enable_music = True # Whether or not music is enabled
enable_audio = True # Whether or not audio should be played
Inv_Slot = 0 # Default inventory slot
enable_program = True # Enables or Disables the program

# Colors, these variables are however rarely used
BLACK = (0, 0, 0) # The RGB code for Black
RED = (255, 0, 0) # The RGB code for Red
GREEN = (0, 255, 0) # The RGB code for Green
BLUE = (0, 0, 255) # The RGB code for Blue
GRAY = (200, 200, 200) # The RGB code for Gray
WHITE = (255, 255, 255) # The RGB code fro White
NaN = ("NaN", "NaN", "NaN") # The RGB code for NaN

# Debugging settings
disable_background = False # Wether the game should load the background image
player_color = (0, 0, 0) # The color of the player's hitbox
block_color = (0, 0, 0) # Default square color
info_color = (150, 150, 150) # Info square color
dialog_color = (255, 255, 255) # Dialog box color
background_color = (128, 0, 128) # The background color of the game
show_debug = False # Enable debugging messages
enable_crash_debug = False # Enables keybind to cause a game crash

# File paths
inventory_path = "Textures/slot/" # Where to pull Inventory and gui textures from
item_path = "Textures/items/" # Where to pull item textures from
environment_audio_path = "Audio/Environment/" # Where to pull environment audio from
environment_path = "Textures/Environment/" # Where to pull environmental textures from
characters_path = "Textures/Characters/" # Where to pull character textures from
transparent_prefix = "transparent_" # The prefix to use when retrieving transparent files
flipped_prefix = "flipped_" # Currently does nothing

# WARNING: Changing these settings might cause issues
size = [500, 500] # The size of the screen
square_size = 20 # How big the default hitbox is
game_border1 = 480 # Maximum cordinates player can be
game_border2 = 0 # Minimum cordinates playerr can be
speed = 10 # How fast the player moves
item_size = 10 # The size of an item's hitbox
fps = 10 # The FPS of the game
inv = [0, 0, 0, 0, 0, 0] # Inventory list
minimum_slot = 80 # The default coordinates of slot 0
gameIcon = pygame.image.load('Textures/Icons/game.png') # Path to game's window icon
