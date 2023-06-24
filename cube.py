from settings import *


class Cube(pygame.sprite.Sprite):
    def __init__(self, pos, x_dir, y_dir, colour=player_colour, size=(tile_size, tile_size)):
        # Initializing Parent Class
        super().__init__()

        # Initializing Core Sprite Variables
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(x_dir, y_dir)

    def update(self, keys):
        self.rect.x += move_speed * self.direction.x
        self.rect.y += move_speed * self.direction.y

    def change_dir(self, dir):
        if self.on_tile():
            self.direction.x = dir.x
            self.direction.y = dir.y

    def on_tile(self):
        if self.rect.x % tile_size == 0 and self.rect.y % tile_size == 0:
            return True
        else:
            return False
