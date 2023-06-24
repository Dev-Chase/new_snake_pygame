# Run this file to play game
from settings import *
from snake import Snake
import sys
from random import randint


if __name__ == '__main__':
    # Pygame Setup
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("New Snake")

    # Sprite Drawing Variables
    screen = pygame.display.set_mode((W, H))
    display = pygame.Surface((W, H))
    screen_offs = pygame.math.Vector2(0, 0)
    screen_shake = 0

    # Text Variables
    font = pygame.font.SysFont('system', 30)
    game_over_text = font.render('Game Over. Press Space to Start.', True, fg_colour)
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

        # Start Screen
        if game_state == game_states["start"]:
            display.blit(start_text, start_text_rect.topleft)
            if keys[pygame.K_SPACE]:
                game_state = game_states["playing"]
                snake.__init__()
                begin_game_state(world_sprites, [snake.body])

        # Playing Screen
        elif game_state == game_states["playing"]:
            snake.update(keys)
            world_sprites.update(keys)
            if snake.out_of_bounds():
                game_state = game_states["game-over"]
                screen_shake = FPS/8  # Screen Shake for an Eighth of a Second
                begin_game_state(world_sprites, [snake.body])

        # Game Over Screen
        elif game_state == game_states["game-over"]:
            display.blit(game_over_text, game_over_text_rect.topleft)
            if keys[pygame.K_SPACE]:
                game_state = game_states["playing"]
                snake.__init__()
                begin_game_state(world_sprites, [snake.body])

        world_sprites.draw(display)

        # Implement Screen Shake
        if screen_shake <= 0:
            screen_shake = 0
        else:
            screen_offs.x = randint(-2, 2)
            screen_offs.y = randint(-2, 2)
            screen_shake -= 1


        # Moving Display on Screen in Case of Screen Shake
        screen.blit(pygame.transform.scale(display, (W, H)), (screen_offs.x, screen_offs.y))

        pygame.display.update()
        clock.tick(FPS)
