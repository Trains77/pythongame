# Modules
import os # For disabling pygame support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide Pygame support prompt
import pygame # For generating some graphical elements
import math, random # For generating random numbers
pygame.init()

# shared.py is meant to be a single place for me to store and modify various variables used by script, as well as storing some settings

# Game Settings
language = "english" # Currently supported languages: english
enable_music = False # Whether or not music is enabled
enable_audio = True # Whether or not audio should be played
enable_program = True # Enables or Disables the program
show_controls = True # Display controls on screen

# Debugging settings
disable_background = False # Wether the game should load the background image
enable_debug = False # Enable debug mode
fallback_lang_only = False # Only use fallback language file



## Modifying settings beyond this point could cause issues, be careful!


# Player data
moved = False # Wether or not the player has moved
disable_controls = False # Wether or not controls are currently enabled
max_health = 19 # Maxinimum health a player can have
health = max_health # Current player health
health_tick = 0 # Internal health tick
poison_duration = 0 # How long the player has poison for
facing = "Left" # Default player rotation

# RGB codes
BLACK = (0, 0, 0) # The RGB code for Black
RED = (255, 0, 0) # The RGB code for Red
GREEN = (0, 255, 0) # The RGB code for Green
BLUE = (0, 0, 255) # The RGB code for Blue
GRAY = (200, 200, 200) # The RGB code for Gray
DARK_GRAY = (50, 50, 50) # The RGB code  for Dark Gray
WHITE = (255, 255, 255) # The RGB code for White


### Internal variables, changing them will cause issues

# Internal Game Variables
size = [500, 500] # The size of the screen
square_size = 20 # How big the default hitbox is
game_border1 = 480 # Maximum cordinates player's coordinates can be
game_border2 = 0 # Minimum cordinates the player's cordinates can be
speed = 10 # The speed of the player
item_size = 10 # The size of an item's hitbox
fps = 20 # The FPS of the game
minimum_slot = 80 # The default coordinates of slot 0
dialog_select = 0 # The default selection for dialog, currently unused
mapid = 0 # Starting map id
system_recommends = "Linux" # The system(s) that the script is verified to work with
version = "0.11.0" # Game version
font1 = pygame.font.SysFont('A totally real font', 20) # Default font for text rendering
appended = False # Used for setting up variables
GameName = "Another Python Game" # The name of the game
song = 'Audio/Music/music1.wav' # Path to music file
spookie = 'Audio/Music/spookie.wav' # Path to spookie music file
Inv_Slot = 0 # Default inventory slot

# File paths
inventory_path = "Textures/slot/" # Where to pull Inventory and gui textures from
item_path = "Textures/items/" # Where to pull item textures from
environment_audio_path = "Audio/Environment/" # Where to pull environment audio from
environment_path = "Textures/Environment/" # Where to pull environmental textures from
characters_path = "Textures/Characters/" # Where to pull character textures from
transparent_prefix = "transparent_" # The prefix to use when retrieving transparent files
flipped_prefix = "flipped_" # The prefix for getting flipped item textures
gameIcon = pygame.image.load('Textures/Icons/game.png') # Path to game's window icon

# Item and object Positions
item_pos = [[250, 275], [50, 300], [99, 450], [250, 250], [3000, 3000], [3000, 3000]]
#           hammer      sword       axe         bow_pos     Banana          Ananab
info_pos = [200, 200] # Default info location
none = [0, 0] # Empty

# Hitbox colors
player_color = (0, 0, 0) # The color of the player's hitbox
block_color = (0, 0, 0) # Default square color
info_color = (150, 150, 150) # Info square color
dialog_color = (255, 255, 255) # Dialog box color
background_color = (128, 0, 128) # The background color of the game

# Enemy Data
enemyPositions = [[350,250], [150, 350]] # All enemy starting positions
enemy_squares = [] # Enemy squares list
enemy_count = 2 # The amount of enemies current enabled
enemy_status = [[1], [1]] # some enamy statuses

# Display Data
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
offscreen = pygame.draw.rect(screen, block_color, [1000,1000,square_size + 10,square_size + 10])
detector_square = offscreen

# Internal Dialog Data
nextdialog = False # Dialog 1
nextdialog2 = False # Dialog 2
nextdialog3 = False # Dialog 3
nextdialog4 = False # Dialog 4
scientist_leaving = False # Whether or not the scientist is leaving

# Internal Inventory and Item data
SelectItem = "NaN" # Selected Item
inv = [0, 0, 0, 0, 0, 0] # Inventory list
bow_slot = [-1, 235] # Slot bow is in
axe_slot = [-1, 235] # Slot Axe is in
hammer_slot = [-1, 235] # Slot hammer is in
sword_slot = [-1, 235] # Slot sword is in
banana_slot = [-1, 235] # Slot banana is in
ananab_slot = [-1, 235] # ni si ananab tols
INV_MIN = 0 # Minimum inventory slot that is allowed by the game
INV_MAX = 4 # Maximum inventory slot that is allowed by the game
item_world_id = [0, 0, 0, 2, 0, 1] # What world an item is in

# Internal Player Data
dead = False # Whether or not the player is dead
playerx = int(math.ceil(random.randint(10,450) / 10.0)) * 10 # Player x cordinates
playery = int(math.ceil(random.randint(10,450) / 10.0)) * 10 # Player y coordinates
player_movement = [1, 1, 1, 1, 1] # left right down up item
score = 0 # Player starting score
velocityY = 0 # Player Y Velocity
jump = 0 # Player jump
last_damage = "generic" # Last type of damage received

# Internal Tree Data
amount_of_trees = 13 # How many trees in Map 0 to spawn
tree_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # The positions of all the trees in world 0
inv_tree_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # The positions of all the trees in world 1
trees_destroyed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,] # The trees that have been destroyed in world 0
inv_trees_destroyed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,] # The trees that have been destroyed in world 1

# Generate Tree coordinates
for i in range(amount_of_trees):
    tree_positions[i] = [int(math.ceil(random.randint(10,450) / 10.0)) * 10, int(math.ceil(random.randint(10,450) / 10.0)) * 10]
    inv_tree_positions[i] = [int(math.ceil(random.randint(10,450) / 10.0)) * 10, int(math.ceil(random.randint(10,450) / 10.0)) * 10]

# Bow and Arrow Functions
arrows_positions = []
arrow_amount = 0
