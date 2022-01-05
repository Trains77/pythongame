# Modules
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

# Game Settings
GameName = "Another Python Game" # The name of the game
song = 'Audio/Music/music1.wav' # Path to music file
spookie = 'Audio/Music/spookie.wav' # Path to spookie music file
enable_music = True # Whether or not music is enabled
enable_audio = True # Whether or not audio should be played
Inv_Slot = 0 # Default inventory slot
enable_program = True # Enables or Disables the program
facing = "Right" # Default player rotation

# Color rgb codes
BLACK = (0, 0, 0) # The RGB code for Black
RED = (255, 0, 0) # The RGB code for Red
GREEN = (0, 255, 0) # The RGB code for Green
BLUE = (0, 0, 255) # The RGB code for Blue
GRAY = (200, 200, 200) # The RGB code for Gray
WHITE = (255, 255, 255) # The RGB code for White
NaN = ("NaN", "NaN", "NaN") # The RGB code for NaN

# Debugging settings
disable_background = False # Wether the game should load the background image
player_color = (0, 0, 0) # The color of the player's hitbox
block_color = (0, 0, 0) # Default square color
info_color = (150, 150, 150) # Info square color
dialog_color = (255, 255, 255) # Dialog box color
background_color = (128, 0, 128) # The background color of the game
show_debug = True # Enable debugging messages
enable_crash_debug = False # Enables keybind to cause a game crash

# Item and object Positions
hammer_pos = [250, 275]
sword_pos = [50, 300]
axe_pos = [99, 450]
bow_pos = [250, 250]
banana_pos = [3000, 3000]
info_pos = [200, 200]

# Trees
tree1 = [450, 450]

# Inventory Stuff
bow_slot = [-1, 235]
axe_slot = [-1, 235]
hammer_slot = [-1, 235]
sword_slot = [-1, 235]
banana_slot = [-1, 235]

# File paths
inventory_path = "Textures/slot/" # Where to pull Inventory and gui textures from
item_path = "Textures/items/" # Where to pull item textures from
environment_audio_path = "Audio/Environment/" # Where to pull environment audio from
environment_path = "Textures/Environment/" # Where to pull environmental textures from
characters_path = "Textures/Characters/" # Where to pull character textures from
transparent_prefix = "transparent_" # The prefix to use when retrieving transparent files
flipped_prefix = "flipped_" # The prefix for getting flipped item textures

# Internal variables, changing them will cause issues
size = [500, 500] # The size of the screen
square_size = 20 # How big the default hitbox is
game_border1 = 480 # Maximum cordinates player's coordinates can be
game_border2 = 0 # Minimum cordinates the player's cordinates can be
speed = 10 # The speed of the player
item_size = 10 # The size of an item's hitbox
fps = 10 # The FPS of the game
inv = [0, 0, 0, 0, 0, 0] # Inventory list
item_world_id = [0, 0, 0, 2, 0] # What world an item is in
minimum_slot = 80 # The default coordinates of slot 0
gameIcon = pygame.image.load('Textures/Icons/game.png') # Path to game's window icon
dialog_select = 0 # The default selection for dialog, currently unused
mapid = 0 # Starting map id
system_recommends = "Linux" # The system(s) that the script is verified to work with
version = "0.08.0" # Game version
INV_MIN = 0 # Minimum inventory slot that is allowed by the game
INV_MAX = 4 # Maximum inventory slot that is allowed by the game
