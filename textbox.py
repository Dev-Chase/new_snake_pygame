from settings import *


class TextBox:
    def __init__(self, content="Hello World!", pos=(W//2, H//2), colour=fg_colour):
        self.font = pygame.font.SysFont('system', 30)
        self.text = self.font.render(content, True, colour)
        self.rect = self.text.get_rect(center=pos)
