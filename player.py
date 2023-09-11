import pygame
from data import LINE_Y


PLAYER_WIDTH = 100
PLAYER_HEIGHT = 140
PLAYER_X = 40


class Player:

    def __init__(self, game_window : pygame.display) -> None:
        self.cordX = PLAYER_X
        self.cordY = LINE_Y - PLAYER_HEIGHT
        self.score = 0
        self.window = game_window
        self.throwCount = 0

    def show(self) -> None:
        player_img = pygame.image.load("player.png")
        player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.window.blit(player_img, (self.cordX, self.cordY))

    def reset(self) -> None:
        self.score = 0
        self.throwCount = 0

    def setDistance(self, dist : int) -> None:
        self.score = dist

    def throwRock(self, rock, power, angle) -> None:
        rock.throw(power, angle)
        self.throwCount += 1

