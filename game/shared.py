# Stuff for variables
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

# Game Settings
disable_background = False # Set whether the game loads the background file
enable_os_restrictions = 0 # Whether to enable strict os checking
credits = 1 # Whether to display credits at startup
size = [500, 500] # The size of the screen
GameName = "Another Python Game" # The window name of the game
square_size = 20 # How big the default square hitbox is
player_color = (0, 0, 0) # The color of the player hitbox
game_border1 = 480 # Maximum cordinates player can go
game_border2 = 0 # Minimum cordinates playerr can go
speed = 10 # How fast the player moves
background_color = (128, 0, 128) # The background color of the game
song = 'Audio/Music/music1.wav' # Where the game's music file is stored
enable_music = 1 # Whether or not the game should play music
info_color = (150, 150, 150) # Info square color
dialog_color = (255, 255, 255) # Dialog box color
fps = 10 # The game's FPS
block_color = (0, 0, 0) # Block Color
gameIcon = pygame.image.load('Textures/Icons/game.png') # Path to game's window icon
item_size = 10 # Item size
item1x = 250 # Item 1 default x position
item1y = 250 # Item 1 default y position
enable_program = True # Enable or Disable the program
