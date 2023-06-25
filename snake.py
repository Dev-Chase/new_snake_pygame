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
        if keys[pygame.K_LEFT] and self.head.dir.x == 0:
            self.direction.x = -1
            self.direction.y = 0
        elif keys[pygame.K_RIGHT] and self.head.dir.x == 0:
            self.direction.x = 1
            self.direction.y = 0

        # Vertical Movement Checks
        if keys[pygame.K_UP] and self.head.dir.y == 0:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and self.head.dir.y == 0:
            self.direction.x = 0
            self.direction.y = 1

        # Insert for loop to Change Body Directions
        # Checking if On Tile
        if self.head.rect.x % tile_size == 0 and self.head.rect.y % tile_size == 0:
            for i in range(1, len(self.body.sprites())):
                # -i = Current Position in Array, Starting from End
                # -i-1 = Cube Position Inherited by Current Position

                self.body.sprites()[-i].rect.topleft = self.body.sprites()[-i-1].rect.topleft-self.body.sprites()[-i].dir*tile_size
                self.body.sprites()[-i].dir = self.body.sprites()[-i-1].dir
                # cube.change_dir(self.body.sprites()[i-1].dir)
            self.body.sprites()[0].change_dir(self.direction)  # (keep trying until on tile)

        # self.body.update()  #TODO fix weird movement (moving at the same time as going to previous cubes pos)
        self.body.update()
        # print([cube.dir for cube in self.body.sprites()])

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
