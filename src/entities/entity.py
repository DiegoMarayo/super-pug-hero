import pygame

class Entity:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surf = None

    def draw(self, window):
        if self.surf is not None:
            window.blit(
                self.surf,
                (self.x, self.y)
            )

    def get_top(self):
        return self.y

    def get_bottom(self):
        return self.y + self.height

    def get_left(self):
        return self.x

    def get_right(self):
        return self.x + self.width

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )