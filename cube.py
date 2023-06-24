from settings import *


class Cube(pygame.sprite.Sprite):
    def __init__(self, pos, x_dir, y_dir, size=(25, 25)):
        # Initializing Parent Class
        super().__init__()

        # Initializing Core Sprite Variables
        self.image = pygame.Surface(size)
        self.image.fill(player_colour)
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(x_dir, y_dir)

    def update(self, keys):
        self.rect.x += move_speed * self.direction.x
        self.rect.y += move_speed * self.direction.y

    def on_tile(self):
        if self.rect.x % self.rect.width == 0 and self.rect.y % self.rect.height == 0:
            return True
        else:
            return False
