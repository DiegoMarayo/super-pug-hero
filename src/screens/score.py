import pygame

from src.const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    C_WHITE, C_GOLDEN, SCORE_OPTION, FONT_NAME
)


class Score:

    def __init__(self, window, repository):

        self.window = window
        self.repository = repository

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

    def draw_scores(self, scores):


        score_font = pygame.font.SysFont(
            FONT_NAME,
            22
        )

        # Cabeçalho
        self.draw_text(24, "RANK", C_GOLDEN, (150, 300))
        self.draw_text(24, "PLAYER", C_GOLDEN, (290, 300))
        self.draw_text(24, "BONES", C_GOLDEN, (430, 300))

        start_y = 350

        for index, row in enumerate(scores):

            player = row[0]
            points = row[1]

            y = start_y + index * 55

            # Rank
            rank = score_font.render(
                f"{index + 1}º",
                True,
                C_WHITE
            )

            # Nome
            name = score_font.render(
                player,
                True,
                C_WHITE
            )

            # Pontos
            bones = score_font.render(
                str(points),
                True,
                C_WHITE
            )

            self.window.blit(rank, (140, y))
            self.window.blit(name, (250, y))
            self.window.blit(bones, (410, y))



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

    def run(self):

        scores = self.repository.top5()

        while True:

            self.window.blit(
                self.surf,
                self.rect
            )

            self.draw_scores(scores)

            self.draw_text(
                40,
                SCORE_OPTION[0],
                C_GOLDEN,
                (
                    WIN_WIDTH // 2,
                    700
                )
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.move_sound.play()

                        return SCORE_OPTION[0]
