# Run this file to play game
from settings import *
from snake import Snake
from cube import Cube
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
    food = Cube(colour=food_colour)
    food_sprite = pygame.sprite.GroupSingle(food)

    # Game State Start
    game_state = game_states["start"]

    # Global Game Variables
    keys = pygame.key.get_pressed()

    while True:
        screen.fill(bg_colour)
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
                # Resetting Snake and Food
                snake.__init__()
                food.__init__(colour=food_colour)
                food.random_pos()
                while snake.head.near(food):
                    food.random_pos()

                # Setting up and Starting the Playing State
                game_state = game_states["playing"]

        # Playing Screen
        elif game_state == game_states["playing"]:
            snake.update(keys)

            # Food Collision Checks
            if snake.hit_cube(food):
                # Make the Snake Grow
                snake.append_cube()
                food.random_pos()

                # Move the Food
                while snake.head.near(food):
                    food.random_pos()

            # Game Over Checks
            if snake.out_of_bounds() or any([snake.hit_cube(section) for section in snake.body.sprites()[1:]]):
                game_state = game_states["game-over"]
                screen_shake = FPS/8  # Screen Shake for an Eighth of a Second

            display.blit(food.image, food.rect.topleft)
            snake.body.draw(display)

        # Game Over Screen
        elif game_state == game_states["game-over"]:
            display.blit(game_over_text, game_over_text_rect.topleft)
            if keys[pygame.K_SPACE]:
                # Resetting Snake and Food
                snake.__init__()
                food.__init__(colour=food_colour)
                food.random_pos()
                while snake.head.near(food):
                    food.random_pos()

                # Setting up and Starting the Playing State
                game_state = game_states["playing"]
            snake.body.draw(display)

        # Implement Screen Shake
        if screen_shake <= 0:
            screen_shake = 0
        else:
            screen_offs.x = randint(-25, 25)/10
            screen_offs.y = randint(-25, 25)/10
            screen_shake -= 1

        # Moving Display on Screen in Case of Screen Shake
        screen.blit(pygame.transform.scale(display, (W, H)), (screen_offs.x, screen_offs.y))

        pygame.display.update()
        clock.tick(FPS)
