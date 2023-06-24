# Run this file to play game
from settings import *
from snake import Snake
import sys
# from random import randint, seed


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
    snake = Snake()

    # Game State Start
    game_state = game_states["start"]
    begin_game_state(world_sprites, [])

    # Global Game Variables
    keys = pygame.key.get_pressed()

    while True:
        display.fill(bg_colour)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == game_states["start"]:
            display.blit(start_text, start_text_rect.topleft)
        elif game_state == game_states["playing"]:
            snake.update(keys)

        world_sprites.update(keys)
        world_sprites.draw(display)

        screen.blit(pygame.transform.scale(display, (W, H)), offs)

        if keys[pygame.K_SPACE] and game_state == game_states["start"]:
            game_state = game_states["playing"]
            begin_game_state(world_sprites, [snake.body])

        pygame.display.update()
        clock.tick(60)
