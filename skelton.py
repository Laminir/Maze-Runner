"""
Maze Runner Game

Maze Runner is a game where a player tries to find treasure
in a maze without running into any monsters lurking in that maze

@author YOUR_NAME
"""
# Note: This skeleton file has a lot of comments in it.
#       Read the comments. They will help give you some
#       direction and understanding of how to use the code
#       that has already been given to you.
#
#       Later if you find them pesky, you can delete them

import turtle
import functools
import random
import time

# NOTE: cannot play sound in replit currently
# import os #for macs
# import winsound #for windows

# Set up window
window = turtle.Screen()
window.title("Maze Runner by YOUR_NAME")
window.bgcolor("black")
window.setup(width=0.3, height=0.5)
width = window.window_width()
height = window.window_height()
window.tracer(0)
turtle.hideturtle()
turtle.penup()
turtle.color("white")
turtle.goto(0, -width//1.7)

# Settings
DEFAULT_TEXT_FILE = "maze_1.txt"
MAZE_TEXT_FILE = "maze_1.txt"
BLOCK_STR = OB = 'X'  # OB --> Out of Bounds
PLAYER_STR = 'C'
TREASURE_STR = 'T'
MONSTER_STR = 'M'
EMPTY_STR = '.'
ALIVE = 0
DEAD = 1
WIN = 2
PLAYER_STATE = ALIVE
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
KEY_LEFT = "a"
KEY_UP = "w"
KEY_RIGHT = "d"
KEY_DOWN = "s"
MONSTER_SPEED_IN_SEC = 1  # in seconds

# Text feedback for winning the game, or losing the game
game_end_list = []
game_win_list = []


# Classes
# --------------------------------------------------------
# A Cell object stores a Turtle object and its coordinates
class Cell:
    def __init__(self, x, y, turtle_obj):
        self.x = x
        self.y = y
        self.turtle_obj = turtle_obj


# A Player is a Cell. It also has a 'state' property,
# where the state keeps track of whether the Player is either
# ALIVE, DEAD, or WIN (the last of which is the brief state
# where the Player has found the treasure and the game is about
# to be over)
class Player(Cell):
    def __init__(self, x, y, turtle_player, state):
        super().__init__(x, y, turtle_player)
        self.state = state


# A Monster is a Cell. It also has the 'direction' property,
# which keeps track of the direction that the monster is
# currently going, either LEFT, UP, DOWN, or RIGHT
class Monster(Cell):
    def __init__(self, x, y, turtle_player, direction=UP):
        super().__init__(x, y, turtle_player)
        self.direction = direction


# Functions
# --------------------------------------------------
# Creates an empty n x n grid of the given data type
def make_grid(size, data_type):
    return [[data_type] * size for _ in range(size)]


# Creates a grid of strings that represent the images
# in the game. These strings are PLAYER_STR, MONSTER_STR,
# TREASURE_STR, BLOCK_STR, and EMPTY_STR, the last of which
# represents empty spaces in the grid
def create_maze(file=DEFAULT_TEXT_FILE):
    cell_maze = [[]]

    file_object = open(file, "r")
    row = 0
    for line in file_object:
        cell_list = line.split(" ")
        for cell in cell_list:
            cell_maze[row].append(cell.strip())
        row += 1
        new_list = []
        cell_maze.append(new_list)

    del cell_maze[len(cell_maze) - 1]
    file_object.close()

    return cell_maze


# This method prints the grid of strings, and can be used as a
# quick reminder what the grid currently looks like in text form
def print_maze_debug(maze):
    for row in maze:
        for col in row:
            print(col, end=' ')
        print("", end="\n")


# Set up grid objects
grid = create_maze(MAZE_TEXT_FILE)
# print_maze_debug(grid)  # For debugging
cell_width = width / len(grid[0])  # Set width based on screen size
cell_height = height / len(grid)  # Set height based on screen size


# Functions to write
# -----------------------------------------------
# Notes: Stage 1 of this project requires you to translate
# the grid of string objects to a visual representation using
# Turtle's images, such as squares, circles, and triangles,
# which we most recently practiced using in Project 3
#
# There are a few things to consider for your own
# implementation:
#
# 1) Game Loop --> What do you want to repeatedly check, run, or
#                  update in the game?
# 2) Initialization --> What things can you do once and then not
#                       have to worry about again?
#                       Eg. You only have to create the player
#                       Turtle object once (since you only get
#                       one life in this game), so you probably
#                       don't want that part in your Game Loop
# 3) Design --> What do you want your game to look like? During
#               preliminary steps like these, you should
#               consider drawing a picture, writing pseudocode,
#               and considering what functionalities your
#               program will need. At the very least, your
#               pseudocode will be collected and should be
#               done BEFORE you start coding!
#
# Here are some suggested functionalities for your program.
# These are listed here for your benefit as a reminder of how
# important it is to split your logic into as many functions
# as is applicable, without being excessive... you should go
# for bite-sized chunks of logic, but not so small as for these
# functions to lose their meaning
#
# Possible functionalities:
# * Printing the blocks of the maze
# * Creating a block object
# * Creating all the block objects
# * Creating the player object
# * Creating a monster object
# * Creating all monster objects
# * Creating the treasure object
# * Displaying all objects
# * ...And possibly more

# Temp variable to allow key-binding code to compile. Creating
# the player object and defining it should probably happen in
# its own function
player_obj = None


# Stage 2 Functions
# -------------------------------------------------
# The stage 2 functions should allow for player movement and
# monster movement. These are the bulk of the logic of the
# program, where objects begin interacting.
#
# For player movement, we are using key-binding on a separate
# thread. This means that the player responds to the keys
# pressed, independent of the main game loop. The key binding
# code can be found below
#
# The monster movement functions can also be placed here.
# You can decide how you want the monsters to move. They can
# be fast or slow, smart, or stupid, random movements, or
# path-finding movements (<-- very hard to implement). I
# recommend a monster that knows how to turn clockwise, and
# that tries to movement in that new direction until they run
# into something, similar to the demo of the program
#
# Monsters and players are constantly changing their x and y
# properties. Keep in mind that these properties correspond
# to the row and col coordinate within your grid. You may also
# need to update the grid of strings if you are depending on
# that grid to be accurate for translating that data into
# where you should be printing your images.
#
# Both players and monsters should not be able to leave the
# bounds of the grid, and both should not be able to walk into
# or through blocks, which act as barriers. I would recommend
# treating the treasure as a barrier as well.
#
# There are many ways to speed up or slow down monster
# movement. I would recommend using the time module, which can
# be used to keep track of the real-time changes, so that
# monsters can move every few seconds, or whatever
# MONSTER_SPEED_IN_SEC is set to


def move(player, key_str):
    pass


# Keyboard binding
window.listen()
window.onkeypress(functools.partial(move, player_obj, KEY_UP), KEY_UP)
window.onkeypress(functools.partial(move, player_obj, KEY_DOWN), KEY_DOWN)
window.onkeypress(functools.partial(move, player_obj, KEY_LEFT), KEY_LEFT)
window.onkeypress(functools.partial(move, player_obj, KEY_RIGHT), KEY_RIGHT)
window.listen()

# Stage 3 Functions
# ---------------------------------------------
# There are some things that we could ignore during the first
# two stages that need to be implemented in this stage. The
# game needs to be able to detect when the player has won or
# lost, and that means detecting when a monster has run into
# a player, or when a player has run into a monster, and when
# the player has run into the treasure
#
# There should also be text that is displayed when the player
# wins or loses. To practice using the random module, for stage
# 3 you need to randomly select from a list of possible
# responses for when the player wins, or when they lose. These
# phrases can be stored in the lists game_end_list and
# game_win_list


def move_monsters():
    pass


# The Game Loop
# ---------------------------------------------
# For Stage 1, our Game Loop can be very simple... we just want
# to update the images on our screen
# For Stage 2, we will want to update the monsters and the
# player. However, the player moves independently of the
# monsters (on a different thread), so really just the monsters
# should be updated in the game loop here
# For Stage 3, the game loop should also check for whether the
# player has won or lost
# For Stage 4 (the bonus stage), depending on what you try
# and implement, you may need to add more to the game loop
start_time = time.time()
while True:
    window.update()

    # Move the monsters
    if time.time() - start_time > MONSTER_SPEED_IN_SEC:
        move_monsters()
        start_time = time.time()

    # Code below for detecting if a player won or lost

turtle.done()
# Currently ^ this code is 'unreachable'... Python
# gives us a warning, but will still allow the
# file to compile without error. You will want
# to find some way to change the condition of
# the game loop, or to find some way to break out
# of the loop
