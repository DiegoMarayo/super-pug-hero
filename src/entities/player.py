import pygame
from src.entities.entity import Entity

class Player(Entity):

    def __init__(self):

        super().__init__(100, 250, 50,50)
        self.speed_y = 0
        self.gravity = 0.5

        self.surf = pygame.image.load('./assets/images/pug1.png').convert_alpha()
        self.surf = pygame.transform.scale(
            self.surf,(
                self.width, self.height
            )
        )
        self.fly_sound = pygame.mixer.Sound(
            "./assets/sounds/menu1.mp3"
        )

        self.fly_sound.set_volume(0.5)

    def update(self):
        self.speed_y += self.gravity
        self.y += self.speed_y

    def fly(self):
        self.fly_sound.play()
        self.speed_y = -10