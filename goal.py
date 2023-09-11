import pygame
import math
from data import LINE_Y, BLACK
from random import randint

GOAL_HEIGHT : int = 60
GOAL_WIDTH : int  = 30


class Goal:

    def __init__(self, game_window : pygame.display) -> None:
        self.cordX = randint(500,1000)
        self.cordY = randint(game_window.get_width()/6, LINE_Y-100)

        self.window = game_window


    def show(self) -> None:
        goal_img = pygame.draw.rect(self.window, BLACK, (self.cordX, self.cordY, GOAL_WIDTH, GOAL_HEIGHT))
        goal_img = pygame.draw.rect(self.window, (0,0,255), (self.cordX, self.cordY, GOAL_WIDTH, GOAL_HEIGHT), 2)
        



    