import pygame

from src.const import PIPE_SPEED
from src.entities.entity import Entity


class Obstacle(Entity):

    def __init__(self, x, y, image):

        # Carrega a imagem temporariamente
        surf = pygame.image.load(image).convert_alpha()

        width = surf.get_width()
        height = surf.get_height()

        # Inicializa a Entity
        super().__init__(
            x,
            y,
            width,
            height
        )

        # Agora atribui a imagem
        self.surf = surf

    def update(self):
        self.x -= PIPE_SPEED

    def reset(self):
        self.x = 650