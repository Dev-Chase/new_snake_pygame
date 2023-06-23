# Run this file to play game
import pygame
from pytiled_parser import world

from settings import *
import sys
# from random import randint, seed


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, size=(25, 25)):
        # Initializing Parent Class
        super().__init__()

        # Initializing Core Sprite Variables
        self.image = pygame.Surface(size)
        self.image.fill(player_colour)
        self.rect = self.image.get_rect(center=pos)


def begin_game_state(surface, sprite_list, new_sprites):
    sprite_list.empty()
    sprite_list.clear(surface, bg_colour)

    for sprite in new_sprites:
        sprite_list.add(sprite)


if __name__ == '__main__':
    # Pygame Setup
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("New Snake")

    # Sprite Drawing Variables
    screen = pygame.display.set_mode((W, H))
    display = pygame.Surface((W, H))
    offs = (0, 0)
    # screen_shake = 0

    # Text Variables
    font = pygame.font.SysFont('system', 30)
    game_over_text = font.render('Game Over.', True, fg_colour)
    start_text = font.render('Press Space to Start', True, fg_colour)

    # Text Rectangles
    game_over_text_rect = game_over_text.get_rect(center=(W//2, H//2))
    start_text_rect = start_text.get_rect(center=(W//2, H//2))

    # Sprite Groups
    world_sprites = pygame.sprite.Group()
    player = pygame.sprite.GroupSingle(Snake((W//2, H//2)))

    # Game State Start
    game_state = game_states["start"]
    begin_game_state(display, world_sprites, [])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill(bg_colour)

        world_sprites.update()
        world_sprites.draw(display)

        if game_state == game_states["start"]:
            display.blit(start_text, start_text_rect.topleft)

        screen.blit(pygame.transform.scale(display, (W, H)), offs)

        pygame.display.update()
        clock.tick(60)
