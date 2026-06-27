import pygame

from src.const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    C_WHITE, C_GOLDEN, SCORE_OPTION
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
            "Lucida Sans Typewriter",
            22
        )

        start_y = 300

        for index, row in enumerate(scores):

            points = row[0]

            text = score_font.render(

                f"{index + 1:>2}°   {points} BONES",

                True,

                C_WHITE

            )



            text_rect=text.get_rect(
                    center=(
                        WIN_WIDTH // 2,
                        start_y + index * 55
                    )
            )

            self.window.blit(text, text_rect)



    def draw_text(
            self,
            size,
            text,
            color,
            center
    ):

        font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
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

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            self.move_sound.play()

                            return SCORE_OPTION[0]
