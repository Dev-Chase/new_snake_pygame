from settings import *
from cube import Cube


class Snake:
    def __init__(self):
        # Creating Snake Variables
        self.head = Cube((W//2, H//2), 1, 0)
        self.body = pygame.sprite.Group(self.head)

        self.direction = pygame.math.Vector2(1, 0)

    def update(self, keys):
        if keys[pygame.K_LEFT] and not self.direction.x == 1:
            self.direction.x = -1
            self.direction.y = 0
        elif keys[pygame.K_RIGHT] and not self.direction.x == -1:
            self.direction.x = 1
            self.direction.y = 0
        elif keys[pygame.K_UP] and not self.direction.y == 1:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and not self.direction.y == -1:
            self.direction.x = 0
            self.direction.y = 1

        # Insert for loop to Change Body Directions
        self.head.direction = self.direction

    def out_of_bounds(self):
        if self.head.rect.x < 0 or self.head.rect.x > W or self.head.rect.y < 0 or self.head.rect.y > H:
            return True
        else:
            return False

    def draw(self, surface):
        self.body.draw(surface)
