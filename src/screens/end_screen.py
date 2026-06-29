import sys
import pygame

from src.const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    C_GOLDEN,
    C_WHITE,
    FONT_NAME
)
from src.utils.assets import Assets


class EndScreen:

    def __init__(
            self,
            window,
            repository,
            score,
            background,
            sound,
            options
    ):

        self.window = window
        self.repository = repository
        self.score = score
        self.options = options

        self.surf = Assets.image(
            background,
            WIN_WIDTH,
            WIN_HEIGHT
        )

        self.rect = self.surf.get_rect(
            left=0,
            top=0
        )

        self.sound = Assets.sound(
            sound,
            0.6
        )

        self.move_sound = Assets.sound(
            "menu1.mp3",
            0.5
        )

        # Nome
        self.player_name = ""

        self.name_confirmed = False

        self.cursor_visible = True
        self.cursor_timer = 0

        self.clock = pygame.time.Clock()

        # Menu
        self.option = 0

        # Fontes
        self.title_font = Assets.font(
            FONT_NAME,
            28,
            bold=True
        )

        self.input_font = Assets.font(
            FONT_NAME,
            36,
            bold=True
        )

        self.help_font = Assets.font(
            FONT_NAME,
            22,
            bold=True
        )

        self.menu_font = Assets.font(
            FONT_NAME,
            30
        )

        self.menu_selected_font = Assets.font(
            FONT_NAME,
            40
        )

    def draw_text(
            self,
            size,
            text,
            color,
            center
    ):

        if size == 40:
            font = self.menu_selected_font
        elif size == 30:
            font = self.menu_font
        else:
            font = Assets.font(
                FONT_NAME,
                size
            )

        surf = font.render(
            text,
            True,
            color
        )

        rect = surf.get_rect(
            center=center
        )

        self.window.blit(
            surf,
            rect
        )

    def draw_name_input(self):
        title = self.title_font.render(
            "ENTER YOUR NAME",
            True,
            C_GOLDEN
        )

        self.window.blit(
            title,
            title.get_rect(
                center=(WIN_WIDTH // 2, 670)
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
                center=(WIN_WIDTH // 2, 750)
            )
        )

        help_text = self.help_font.render(
            "PRESS ENTER",
            True,
            C_GOLDEN
        )

        self.window.blit(
            help_text,
            help_text.get_rect(
                center=(WIN_WIDTH // 2, 830)
            )
        )

    def update_cursor(self):
        self.cursor_timer += 1

        if self.cursor_timer >= 30:
            self.cursor_visible = not self.cursor_visible

            self.cursor_timer = 0

    def save_player(self):

        if self.player_name.strip() == "":
            self.player_name = "PLAYER"

        self.repository.save(
            self.player_name,
            self.score
        )

        self.name_confirmed = True

    def run(self):

        pygame.mixer_music.stop()

        self.sound.play()

        while True:

            self.update_cursor()

            self.window.blit(
                self.surf,
                self.rect
            )

            # ============================
            # ESTADO 1 -> Digitar o nome
            # ============================

            if not self.name_confirmed:

                self.draw_name_input()

            # ============================
            # ESTADO 2 -> Mostrar menu
            # ============================

            else:

                for i in range(len(self.options)):

                    if i == self.option:

                        self.draw_text(
                            40,
                            self.options[i],
                            C_GOLDEN,
                            (
                                WIN_WIDTH // 2,
                                700 + i * 60
                            )
                        )

                    else:

                        self.draw_text(
                            30,
                            self.options[i],
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

                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    # ===================================
                    # DIGITAÇÃO DO NOME
                    # ===================================

                    if not self.name_confirmed:

                        if event.key == pygame.K_RETURN:

                            self.move_sound.play()

                            self.save_player()

                        elif event.key == pygame.K_BACKSPACE:

                            self.move_sound.play()

                            self.player_name = self.player_name[:-1]

                        else:

                            if (
                                    len(self.player_name) < 10
                                    and event.unicode.isalnum()
                            ):
                                self.move_sound.play()

                                self.player_name += event.unicode.upper()

                    # ===================================
                    # MENU
                    # ===================================

                    else:

                        if event.key == pygame.K_DOWN:

                            self.move_sound.play()

                            if self.option < len(self.options) - 1:

                                self.option += 1

                            else:

                                self.option = 0

                        elif event.key == pygame.K_UP:

                            self.move_sound.play()

                            if self.option > 0:

                                self.option -= 1

                            else:

                                self.option = len(self.options) - 1

                        elif event.key == pygame.K_RETURN:

                            self.sound.stop()

                            return self.options[self.option]

            self.clock.tick(60)