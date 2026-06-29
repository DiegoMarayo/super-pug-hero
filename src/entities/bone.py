import pygame

from src.const import PIPE_SPEED
from src.entities.entity import Entity
from src.utils.assets import Assets


class Bone(Entity):

    def __init__(self):
        self.active = True
        super().__init__(
            700,
            400,
            40,
            40
        )

        self.surf = Assets.image("bone.png")

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