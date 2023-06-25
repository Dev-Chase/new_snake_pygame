from settings import *


class Cube(pygame.sprite.Sprite):
    # Class Constructor
    def __init__(self, pos=(tile_size*(W//tile_size//2), tile_size*(H//tile_size//2)), colour=player_colour, size=(tile_size, tile_size)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)


class Snake:
    # Class Constructor
    def __init__(self):
        self.desired_direction = pygame.math.Vector2(0, 0)
        self.body = [Cube()]

    # Method to Run Every Frame
    def update(self):
        keys = pygame.key.get_pressed()

    # Drawing Method
    def display(self, surface):
        for item in self.body:
            surface.blit(item.image, item.rect.topleft)
            self.on_tile()

    # On Tile Check Method
    def on_tile(self):
        if self.body[0].rect.x % tile_size == 0 and self.body[0].rect.y % tile_size == 0:
            return True
        return False

    # Crash Check
    def crashed(self):
        if any([self.body[0].rect.colliderect(item) for item in self.body[1::]]):
            return True
        return False

    # Bounds Check
    def in_bounds(self):
        if self.body[0].rect.top > -1 and self.body[0].rect.left > -1 and self.body[0].rect.right < W+1 and self.body[0].rect.bottom < H+1:
            return True
        return False

    def move_step(self, d):
        for item in self.body:
            item.rect.topleft += d * tile_size
