import pygame

from src.const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    C_GOLDEN,
    C_WHITE,
    FONT_NAME
)


class NameInput:

    def __init__(self, window):

        self.window = window

        self.surf = pygame.image.load(
            "./assets/images/name_input.png"
        ).convert_alpha()

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

        self.player_name = ""

        self.clock = pygame.time.Clock()

        self.cursor_visible = True
        self.cursor_timer = 0

        # Fontes (criadas apenas uma vez)
        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            28,
            bold=True
        )

        self.input_font = pygame.font.SysFont(
            FONT_NAME,
            36,
            bold=True
        )

        self.help_font = pygame.font.SysFont(
            FONT_NAME,
            22,
            bold=True
        )

    def draw(self):

        self.window.blit(
            self.surf,
            self.rect
        )

        title = self.title_font.render(
            "ENTER YOUR NAME",
            True,
            C_GOLDEN
        )

        sub_title = self.help_font.render(
            "PRESS ENTER TO CONTINUE",
            True,
            C_GOLDEN
        )

        self.window.blit(
            title,
            title.get_rect(
                center=(WIN_WIDTH // 2, 250)
            )
        )

        self.window.blit(
            sub_title,
            sub_title.get_rect(
                center=(WIN_WIDTH // 2, 510)
            )
        )

        cursor = "_" if self.cursor_visible else ""

        name = self.input_font.render(
            self.player_name + cursor,
            True,
            C_WHITE
        )

        self.window.blit(
            name,
            name.get_rect(
                center=(WIN_WIDTH // 2, 380)
            )
        )

        pygame.display.flip()

    def run(self):

        while True:

            self.cursor_timer += 1

            if self.cursor_timer >= 30:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0

            self.draw()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    # Confirma o nome
                    if event.key == pygame.K_RETURN:

                        self.move_sound.play()

                        if self.player_name.strip() == "":
                            self.player_name = "PLAYER"

                        return self.player_name

                    # Apaga um caractere
                    elif event.key == pygame.K_BACKSPACE:

                        self.move_sound.play()

                        self.player_name = self.player_name[:-1]

                    # Digita caracteres
                    else:

                        if (
                            len(self.player_name) < 10
                            and event.unicode.isalnum()
                        ):

                            self.move_sound.play()

                            self.player_name += event.unicode.upper()

            self.clock.tick(60)