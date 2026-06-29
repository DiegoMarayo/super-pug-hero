import pygame
from src.entities.entity import Entity
from src.utils.assets import Assets


class Player(Entity):

    def __init__(self):

        super().__init__(100, 250, 50, 50)
        self.speed_y = 0
        self.gravity = 0.5

        self.surf_up = Assets.image("pug_up.png")
        self.surf_idle = Assets.image("pug_idle.png")
        self.surf_down = Assets.image("pug_down.png")

        self.surf_up = pygame.transform.scale(
            self.surf_up,
            (self.width, self.height)
        )

        self.surf_idle = pygame.transform.scale(
            self.surf_idle,
            (self.width, self.height)
        )

        self.surf_down = pygame.transform.scale(
            self.surf_down,
            (self.width, self.height)
        )

        # Sprite inicial
        self.surf = self.surf_idle
        self.fly_sound = Assets.sound("menu1.mp3", 0.5)

    def update(self):

        self.speed_y += self.gravity
        self.y += self.speed_y

        if self.speed_y < -2:
            self.surf = self.surf_up

        elif self.speed_y > 2:
            self.surf = self.surf_down

        else:
            self.surf = self.surf_idle

    def fly(self):
        self.fly_sound.play()
        self.speed_y = -10
