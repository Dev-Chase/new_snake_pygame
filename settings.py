import pygame
W = 750
H = 600

# Global Data goes here
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
    "purple": (130, 56, 209)
}

bg_colour = colours['black']
fg_colour = colours['white']
player_colour = colours['red']

tile_size = 25
move_speed = 5

game_states = {
    "start": 0,
    "playing": 1,
    "pause": 2,
    "game-over": 3
}


def begin_game_state(sprite_list, new_sprites):
    sprite_list.empty()
    # sprite_list.clear(surface, bg_colour)

    for sprite in new_sprites:
        sprite_list.add(sprite)
