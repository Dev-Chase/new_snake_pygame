from settings import *


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
        self.dir.x = d.x
        self.dir.y = d.y

    # Randomize Position of Cube
    def go_to(self, dest):
        self.rect.topleft = dest

    # Near Other Cube Check
    def near(self, other_cube):
        if abs(self.rect.centerx - other_cube.rect.centerx) >= tile_size * 1.5 and abs(
                self.rect.centery - other_cube.rect.centery) >= tile_size * 1.5:
            return False
        return True
