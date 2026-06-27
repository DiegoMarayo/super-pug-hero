import pygame
from src.entities.entity import Entity

class Player(Entity):

    def __init__(self):

        super().__init__(100, 250, 50,50)
        self.speed_y = 0
        self.gravity = 0.5

        self.surf_up = pygame.image.load(
            "./assets/images/pug_up.png"
        ).convert_alpha()

        self.surf_idle = pygame.image.load(
            "./assets/images/pug_idle.png"
        ).convert_alpha()

        self.surf_down = pygame.image.load(
            "./assets/images/pug_down.png"
        ).convert_alpha()

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
        self.fly_sound = pygame.mixer.Sound(
            "./assets/sounds/menu1.mp3"
        )

        self.fly_sound.set_volume(0.5)

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