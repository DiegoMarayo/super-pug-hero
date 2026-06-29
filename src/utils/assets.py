import os
import pygame


class Assets:

    IMAGE_PATH = "./assets/images"
    SOUND_PATH = "./assets/sounds"

    @staticmethod
    def image(filename, width=None, height=None):

        path = os.path.join(
            Assets.IMAGE_PATH,
            filename
        )

        image = pygame.image.load(path).convert_alpha()

        if width is not None and height is not None:

            image = pygame.transform.scale(
                image,
                (width, height)
            )

        return image

    @staticmethod
    def sound(filename, volume=1.0):

        path = os.path.join(
            Assets.SOUND_PATH,
            filename
        )

        sound = pygame.mixer.Sound(path)

        sound.set_volume(volume)

        return sound

    @staticmethod
    def music(filename):
        pygame.mixer_music.load(
            os.path.join(
                Assets.SOUND_PATH,
                filename
            )
        )

    @staticmethod
    def font(name, size, bold=False):

        return pygame.font.SysFont(
            name,
            size,
            bold=bold
        )