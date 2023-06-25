# Imports
import pygame
from random import randint

# Player Sizing
tile_size = 24
move_speed = 4

# Big Picture Game Variables
W = tile_size*20
H = tile_size*18
FPS = 35

game_states = {
    "start": 0,
    "playing": 1,
    "paused": 2,
    "game-over": 3
}

# Global Colour Variables
colours = {
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "blue": (0, 0, 128),
    "red": (255, 0, 0),
    "yellow": (242, 255, 0),
    "black": (0, 0, 0),
    "grey": (117, 117, 116),
    "aqua": (0, 255, 255),
    "light-pink": (255, 182, 193),
    "orange": (255, 153, 0),
    "lightblue": (70, 136, 242),
    "light-green": (33, 166, 38),
    "purple": (130, 56, 209),
    "dark-red": (112, 12, 12),
    "lighter-red": (158, 13, 13)
}

bg_colour = colours['black']
fg_colour = colours['white']
player_colour = colours['red']
food_colour = colours['green']


# Global Functions
def random_pos():
    return pygame.math.Vector2(randint(2, W - tile_size - 2), randint(int(tile_size*1.25), H - tile_size - 2))


def get_high_score():
    with open("highscore.txt", "r") as file:
        return int(file.readlines()[-1])


def write_high_score(val):
    with open("highscore.txt", "a") as file:
        file.write(f"\n{val}")

