import pygame

from src.const import (
    WIN_WIDTH,
    WIN_HEIGHT, C_GOLDEN, C_WHITE
)


class NameInput:

    def __init__(self, window):

        self.window = window

        self.surf = pygame.image.load(
            "./assets/images/score.png"
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

    def draw(self):

        self.window.blit(
            self.surf,
            self.rect
        )

        title_font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            28,
            bold=True
        )

        input_font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            36,
            bold=True
        )

        title = title_font.render(
            "ENTER YOUR NAME",
            True,
            C_GOLDEN
        )

        self.window.blit(
            title,
            title.get_rect(
                center=(WIN_WIDTH // 2, 300)
            )
        )

        cursor = "_" if self.cursor_visible else ""

        name = input_font.render(
            self.player_name + cursor,
            True,
            C_WHITE
        )

        self.window.blit(
            name,
            name.get_rect(
                center=(WIN_WIDTH // 2, 420)
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

                        self.player_name = self.player_name[:-1]

                    # Digita caracteres
                    else:

                        if (
                                len(self.player_name) < 10
                                and event.unicode.isprintable()
                                and event.unicode != ""
                        ):
                            self.player_name += event.unicode.upper()

            self.clock.tick(60)
