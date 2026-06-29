import pygame
import sys

from src.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from src.database.init_db import init_database
from src.screens.gameover import GameOver
from src.screens.menu import Menu
from src.screens.gameplay import GamePlay
from src.screens.victory import Victory
from src.repositories.score_repository import ScoreRepository
from src.screens.score import Score


class Game:
    def __init__(self):
        pygame.init()
        init_database()
        self.repository = ScoreRepository()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("SUPER PUG HERO")

    def run(self):

        while True:

            menu = Menu(self.window)
            option = menu.run()

            if option == MENU_OPTION[0]:

                restart = True

                while restart:

                    gameplay = GamePlay(self.window)
                    result = gameplay.run()

                    if result == "GAME_OVER":

                        game_over = GameOver(
                            self.window,
                            self.repository,
                            gameplay.score
                        )

                        option = game_over.run()

                        if option == "TRY AGAIN":
                            restart = True
                        else:
                            restart = False



                    elif result == "VICTORY":

                        victory = Victory(
                            self.window,
                            self.repository,
                            gameplay.score
                        )

                        option = victory.run()

                        if option == "PLAY AGAIN":

                            continue

                        else:

                            restart = False



            elif option == MENU_OPTION[1]:

                score_screen = Score(self.window,self.repository)

                score_screen.run()

            elif option == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
