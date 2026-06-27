import pygame

from src.const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    C_GOLDEN,
    C_WHITE, VICTORY_OPTION, FONT_NAME
)


class Victory:

    def __init__(self, window):

        self.window = window

        self.surf = pygame.image.load(
            "./assets/images/victory.png"
        )

        self.surf = pygame.transform.scale(
            self.surf,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.rect = self.surf.get_rect(
            left=0,
            top=0
        )

        self.move_sound = pygame.mixer.Sound(
            "./assets/sounds/menu1.mp3"
        )

        self.move_sound.set_volume(0.5)

        self.victory_sound = pygame.mixer.Sound(
            "./assets/sounds/victory.mp3"
        )

        self.victory_sound.set_volume(0.6)

    def run(self):

        option = 0

        pygame.mixer_music.stop()

        self.victory_sound.play()

        while True:

            self.window.blit(
                self.surf,
                self.rect
            )

            # Desenha opções
            for i in range(len(VICTORY_OPTION)):

                if i == option:

                    self.draw_text(
                        40,
                        VICTORY_OPTION[i],
                        C_GOLDEN,
                        (
                            WIN_WIDTH // 2,
                            700 + i * 60
                        )
                    )

                else:

                    self.draw_text(
                        30,
                        VICTORY_OPTION[i],
                        C_WHITE,
                        (
                            WIN_WIDTH // 2,
                            700 + i * 60
                        )
                    )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:

                        self.move_sound.play()

                        if option < len(VICTORY_OPTION) - 1:
                            option += 1
                        else:
                            option = 0

                    elif event.key == pygame.K_UP:

                        self.move_sound.play()

                        if option > 0:
                            option -= 1
                        else:
                            option = len(VICTORY_OPTION) - 1

                    elif event.key == pygame.K_RETURN:
                        self.victory_sound.stop()
                        return VICTORY_OPTION[option]

    def draw_text(
            self,
            size,
            text,
            color,
            center
    ):

        font = pygame.font.SysFont(
            FONT_NAME,
            size
        )

        surf = font.render(
            text,
            True,
            color
        ).convert_alpha()

        rect = surf.get_rect(
            center=center
        )

        self.window.blit(
            surf,
            rect
        )