from src.const import PIPE_SPEED
from src.entities.entity import Entity
from src.utils.assets import Assets


class Obstacle(Entity):

    def __init__(self, x, y, image):

        surf = Assets.image(image)

        width = surf.get_width()
        height = surf.get_height()

        super().__init__(
            x,
            y,
            width,
            height
        )

        self.surf = surf

    def update(self):
        self.x -= PIPE_SPEED
