import pygame

from src.const import WIN_WIDTH, PIPE_SPEED
from src.entities.entity import Entity


class Floor(Entity):

    def __init__(self):

        super().__init__(
            0,
            950,
            WIN_WIDTH,
            74
        )

        self.surf = pygame.image.load(
            "./assets/images/floor.png"
        ).convert_alpha()

        self.surf = pygame.transform.scale(
            self.surf,
            (
                self.width,
                self.height
            )
        )

        # Duas cópias do chão
        self.x1 = 0
        self.x2 = self.width

    def update(self):

        self.x1 -= PIPE_SPEED
        self.x2 -= PIPE_SPEED

        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width

        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width

    def draw(self, window):

        window.blit(
            self.surf,
            (self.x1, self.y)
        )

        window.blit(
            self.surf,
            (self.x2, self.y)
        )