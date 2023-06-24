from settings import *
from random import randint


class Cube(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), facing=pygame.math.Vector2(0, 0), colour=player_colour, size=(tile_size, tile_size)):
        # Initializing Parent Class
        super().__init__()

        # Initializing Core Sprite Variables
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)
        self.dir = facing

    def update(self):
        self.rect.x += move_speed * self.dir.x
        self.rect.y += move_speed * self.dir.y

    # Changing Direction
    def change_dir(self, d):
        if self.rect.x % tile_size == 0 and self.rect.y % tile_size == 0:
            print("changing")
            self.dir.x = d.x
            self.dir.y = d.y
            return False
        return True

    # Randomize Position of Cube
    def random_pos(self):
        self.rect.x = randint(2, W-tile_size-2)
        self.rect.y = randint(2, H-tile_size-2)

    # Near Other Cube Check
    def near(self, other_cube):
        if abs(self.rect.centerx - other_cube.rect.centerx) >= tile_size * 1.5 and abs(
                self.rect.centery - other_cube.rect.centery) >= tile_size * 1.5:
            return False
        return True
