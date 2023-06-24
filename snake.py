from settings import *
from cube import Cube


class Snake:
    def __init__(self):
        # Creating Snake Variables
        self.head = Cube((tile_size*(W//2//tile_size), tile_size*(H//2//tile_size)), 1, 0)
        self.body = pygame.sprite.Group(self.head)

        self.direction = pygame.math.Vector2(1, 0)

    def reset(self):
        pass

    def update(self, keys):
        # Horizontal Movement Checks
        if keys[pygame.K_LEFT] and not self.head.direction.x == 1:
            self.direction.x = -1
            self.direction.y = 0
        elif keys[pygame.K_RIGHT] and not self.head.direction.x == -1:
            self.direction.x = 1
            self.direction.y = 0

        # Vertical Movement Checks
        if keys[pygame.K_UP] and not self.head.direction.y == 1:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and not self.head.direction.y == -1:
            self.direction.x = 0
            self.direction.y = 1

        # Insert for loop to Change Body Directions
        self.head.change_dir(self.direction)  # (keep trying every frame until on tile)

    # Out of Bounds Check
    def out_of_bounds(self):
        if self.head.rect.left < 0 or self.head.rect.right > W or self.head.rect.top < 0 or self.head.rect.bottom > H:
            return True
        else:
            return False

    # Cube Hit Check
    def hit_cube(self, cube):
        return self.head.rect.colliderect(cube.rect)

    # Snake Growing Function  #TODO Implement
    def append_cube(self):
        pass

    def draw(self, surface):
        self.body.draw(surface)
