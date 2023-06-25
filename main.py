# Run this file to play game
from settings import *
from snake import Snake
# from cube import Cube
from textbox import TextBox
import sys


if __name__ == '__main__':
    # Pygame Setup
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("New Snake")

    # Display and Sprite Variables
    screen = pygame.display.set_mode((W, H))
    display = pygame.Surface((W, H))
    screen_offs = pygame.math.Vector2(0, 0)
    screen_shake = 0
    snake = Snake()

    # Text Boxes
    text_box = TextBox("Press Space to Start")

    # Game State Start
    game_state = game_states["start"]

    while True:
        display.fill(bg_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_state != game_states["playing"]:
                    # Setting up and Starting the Playing State
                    game_state = game_states["playing"]
                    snake.__init__()
                elif game_states["playing"]:
                    if event.key == pygame.K_f:
                        snake.grow()

        # Start Screen
        if game_state == game_states["start"]:
            display.blit(text_box.text, text_box.rect.topleft)

        # Playing Screen
        elif game_state == game_states["playing"]:
            # Food Collision
            # if pygame.key.get_pressed()[pygame.K_f]:
            #     snake.grow()

            # Game Over Checks
            if pygame.key.get_pressed()[pygame.K_k]:
                text_box.__init__("Game Over. Press Space to Start.")
                game_state = game_states["game-over"]
                screen_shake = FPS/8  # Screen Shake for an Eighth of a Second

            # Updating
            snake.update()

            # Drawing
            snake.draw(display)

        # Game Over Screen
        elif game_state == game_states["game-over"]:
            display.blit(text_box.text, text_box.rect.topleft)

            # Drawing
            snake.draw(display)

        # Implement Screen Shake
        if screen_shake <= 0:
            screen_shake = 0
            screen_offs.x = 0
            screen_offs.y = 0
        else:
            screen_offs.x = randint(-22, 22)/10
            screen_offs.y = randint(-22, 22)/10
            screen_shake -= 1

        # Moving Placing Display on Screen According to Screen Shake Offsets
        screen.blit(pygame.transform.scale(display, (W, H)), (screen_offs.x, screen_offs.y))

        pygame.display.update()
        clock.tick(FPS)
