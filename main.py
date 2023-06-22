# Run this file to play game
from settings import *
import sys
# from random import randint, seed

if __name__ == '__main__':
    # Pygame Setup
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    # screenshake = 0
    offs = (0, 0)
    display = pygame.Surface((W, H))
    clock = pygame.time.Clock()
    game_name = "New Snake"
    pygame.display.set_caption(game_name)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill(bg_colour)

        # world.update()

        screen.blit(pygame.transform.scale(display, (W, H)), offs)

        pygame.display.update()
        clock.tick(60)
