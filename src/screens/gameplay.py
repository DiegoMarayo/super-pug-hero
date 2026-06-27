import pygame
import random

from src.const import (
    PIPE_GAP,
    PIPE_START_X, C_GOLDEN, WIN_SCORE, BACKGROUND_SPEED, WIN_WIDTH, WIN_HEIGHT, GAME_OVER_DELAY, VICTORY_DELAY,
    FONT_NAME,
)
from src.entities.bone import Bone
from src.entities.player import Player
from src.entities.floor import Floor
from src.entities.obstacle import Obstacle


class GamePlay:

    def __init__(self, window):

        self.window = window
        self.clock = pygame.time.Clock()
        self.bone = Bone()
        self.score = 0
        self.bg1_x = 0
        self.bg2_x = WIN_WIDTH
        self.score_font = pygame.font.SysFont(
            FONT_NAME,
            36,
            bold=True
        )

        self.background1 = pygame.image.load(
            "./assets/images/bg1.png"
        ).convert_alpha()

        self.background2 = pygame.image.load(
            "./assets/images/bg2.png"
        ).convert_alpha()

        self.background1 = pygame.transform.scale(
            self.background1,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.background2 = pygame.transform.scale(
            self.background2,
            (WIN_WIDTH, WIN_HEIGHT)
        )
        self.bg_x1 = 0
        self.bg_x2 = WIN_WIDTH

        self.player = Player()
        self.floor = Floor()

        self.obstacle_top = Obstacle(
            PIPE_START_X,
            0,
            "./assets/images/pipe_top.png"
        )

        self.obstacle_bottom = Obstacle(
            PIPE_START_X,
            0,
            "./assets/images/pipe_bottom.png"
        )

        # cria o primeiro obstáculo
        self.reset_obstacles()

    def update_background(self):

        self.bg1_x -= BACKGROUND_SPEED
        self.bg2_x -= BACKGROUND_SPEED

        if self.bg1_x <= - WIN_WIDTH:
            self.bg1_x = self.bg2_x + WIN_WIDTH

        if self.bg2_x <= -WIN_WIDTH:
            self.bg2_x = self.bg1_x + WIN_WIDTH

    def reset_obstacles(self):

        gap_y = random.randint(250, 600)

        self.obstacle_top.x = PIPE_START_X
        self.obstacle_bottom.x = PIPE_START_X

        self.obstacle_top.y = (
                gap_y - self.obstacle_top.height
        )

        self.obstacle_bottom.y = (
                gap_y + PIPE_GAP
        )
        gap_top = self.obstacle_top.get_bottom()
        gap_bottom = self.obstacle_bottom.get_top()

        self.bone.y = (
                (gap_top + gap_bottom) // 2
                - self.bone.height // 2
        )
        self.bone.x = PIPE_START_X + 25
        self.bone.active = True

    def draw_score(self):

        text = self.score_font.render(
            f"BONES: {self.score}",
            True,
            C_GOLDEN
        )

        self.window.blit(text, (20, 20))


    def game_over(self):

        pygame.mixer_music.stop()

        pygame.time.delay(GAME_OVER_DELAY)

        return "GAME_OVER"


    def victory(self):

        pygame.mixer_music.stop()

        pygame.time.delay(VICTORY_DELAY)

        return "VICTORY"


    def run(self):
        pygame.mixer_music.load(
            "./assets/sounds/gameplay.mp3"
        )

        pygame.mixer_music.play(-1)

        while True:

            # ---------------- Eventos ----------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return

                    if event.key == pygame.K_SPACE:
                        self.player.fly()

            # ---------------- Atualizações ----------------

            self.update_background()
            self.player.update()

            self.obstacle_top.update()
            self.obstacle_bottom.update()

            if self.obstacle_top.get_right() < 0:
                self.reset_obstacles()

            # ---------------- Colisões ----------------

            if self.player.get_bottom() >= self.floor.get_top():
                return self.game_over()


            if self.player.get_top() <= 0:
                return self.game_over()


            player_rect = self.player.get_rect()

            if (
                    self.bone.active and
                    player_rect.colliderect(self.bone.get_rect())
            ):
                self.bone.active = False
                self.score += 1

            if self.score >= WIN_SCORE:
                return self.victory()

            if player_rect.colliderect(
                    self.obstacle_top.get_rect()):
                return self.game_over()

            if player_rect.colliderect(
                    self.obstacle_bottom.get_rect()):
                return self.game_over()

            # ---------------- Desenho ----------------

            self.window.blit(self.background1,(self.bg1_x, 0))
            self.window.blit(self.background2,(self.bg2_x, 0))
            self.obstacle_top.draw(self.window)
            self.obstacle_bottom.draw(self.window)
            self.bone.update()
            self.bone.draw(self.window)
            self.floor.update()
            self.floor.draw(self.window)
            self.player.draw(self.window)
            self.draw_score()
            pygame.display.flip()

            self.clock.tick(60)