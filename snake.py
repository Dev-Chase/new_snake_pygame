from settings import *
from cube import Cube


class Snake:
    def __init__(self):
        # Creating Snake Variables
        self.head = Cube((tile_size*(W//2//tile_size), tile_size*(H//2//tile_size)), pygame.math.Vector2(1, 0))
        self.body = pygame.sprite.Group(self.head)

        self.direction = pygame.math.Vector2(1, 0)
        self.should_change = False

    def update(self, keys):
        # Horizontal Movement Checks
        if keys[pygame.K_LEFT] and not self.head.dir.x == 1:  # TODO Existing Movement Checks
            self.direction.x = -1
            self.direction.y = 0
            self.should_change = True
        elif keys[pygame.K_RIGHT] and not self.head.dir.x == -1:
            self.direction.x = 1
            self.direction.y = 0
            self.should_change = True

        # Vertical Movement Checks
        if keys[pygame.K_UP] and not self.head.dir.y == 1:
            self.direction.x = 0
            self.direction.y = -1
            self.should_change = True
        elif keys[pygame.K_DOWN] and not self.head.dir.y == -1:
            self.direction.x = 0
            self.direction.y = 1
            self.should_change = True

        # Insert for loop to Change Body Directions
        if self.should_change:
            self.should_change = self.head.change_dir(self.direction)  # (keep trying until on tile)

        self.body.update()  #TODO fix weird movement

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
        last_cube = self.body.sprites()[-1]
        self.body.add(Cube(pos=last_cube.rect.topleft-last_cube.dir*tile_size, facing=last_cube.dir))
