from src.const import VICTORY_OPTION
from src.screens.end_screen import EndScreen


class Victory(EndScreen):

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
            "victory.png",
            "victory.mp3",
            VICTORY_OPTION
        )