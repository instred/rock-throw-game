from data import WINDOW_WIDTH, BLACK, LINE_Y
from pygame import draw


WALL_Y : int = 0
WALL_WIDTH : int = 20
WALL_X : int = WINDOW_WIDTH - WALL_WIDTH
WALL_HEIGHT : int = LINE_Y

class Wall:

    def __init__(self, game_window) -> None:
        self.cordX = WALL_X
        self.cordY = WALL_Y
        self.width = WALL_WIDTH
        self.height = WALL_HEIGHT
        self.window = game_window

    def show(self) -> None:
        wall_img = draw.rect(self.window, BLACK, (self.cordX, self.cordY, self.width, self.height))

    def collideRight(self, rock):
        if (rock.cordX + rock.radius > self.cordX):
            rock.bounces += 1
            return True
        return False