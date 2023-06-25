from settings import *


class Cube(pygame.sprite.Sprite):
    # Class Constructor
    def __init__(self, pos=(tile_size*(W//tile_size//2), tile_size*(H//tile_size//2)), colour=player_colour, size=(tile_size, tile_size), x=0, y=0):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(x, y)

    # Direction Change Method
    def look_at(self, x, y):
        self.direction.x = x
        self.direction.y = y


class Snake:
    # Class Constructor
    def __init__(self):
        self.desired_x = 0
        self.desired_y = 0
        self.should_change = False
        self.body = [Cube(x=1)]

    # Method to Run Every Frame
    def update(self):
        # Getting Current Pressed Keys
        keys = pygame.key.get_pressed()

        # Horizontal Movement Checks
        if keys[pygame.K_LEFT] and not self.body[0].direction.x:
            self.change_dir(-1, 0)
        elif keys[pygame.K_RIGHT] and not self.body[0].direction.x:
            self.change_dir(1, 0)

        # Vertical Movement Checks
        if keys[pygame.K_UP] and not self.body[0].direction.y:
            self.change_dir(0, -1)
        elif keys[pygame.K_DOWN] and not self.body[0].direction.y:
            self.change_dir(0, 1)

        # Changing Snake Directions if Requested
        if self.on_tile() and self.should_change:  # Only if on Tile
            self.body[0].look_at(self.desired_x, self.desired_y)
            self.should_change = False
        
        # Moving Snake
        self.move()

    # Changing Directions Method
    def change_dir(self, x, y):
        self.should_change = True
        self.desired_x = x
        self.desired_y = y

    # Drawing Method
    def draw(self, surface):
        for item in self.body:
            surface.blit(item.image, item.rect.topleft)
            self.on_tile()

    # Method for Growing Snake after Collision w/ Food
    def grow(self):
        # print("added")
        pass

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

    # Snake Movement Method
    def move(self):
        self.body[0].rect.topleft += self.body[0].direction*move_speed
