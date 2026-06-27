import pygame

from src.const import PIPE_SPEED
from src.entities.entity import Entity

class Bone(Entity):

    def __init__(self):
        self.active = True
        super().__init__(
            700,
            400,
            40,
            40
        )

        self.surf = pygame.image.load(
            "./assets/images/bone.png"
        ).convert_alpha()

        self.surf = pygame.transform.scale(
            self.surf,
            (
                self.width,
                self.height
            )
        )

    def draw(self, window):
        if self.active:
            super().draw(window)

    def update(self):
        if self.active:
            self.x -= PIPE_SPEED