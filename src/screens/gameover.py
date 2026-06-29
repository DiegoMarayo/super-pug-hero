from src.const import GAME_OVER_OPTION
from src.screens.end_screen import EndScreen


class GameOver(EndScreen):

    def __init__(
            self,
            window,
            repository,
            score
    ):

        super().__init__(
            window,
            repository,
            score,
            "game_over.png",
            "game_over.mp3",
            GAME_OVER_OPTION
        )