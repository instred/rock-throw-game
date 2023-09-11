
import math
from pygame import draw, display
from player import PLAYER_X, PLAYER_HEIGHT
from data import LINE_Y, BLACK
from goal import GOAL_HEIGHT, GOAL_WIDTH

ROCK_RADIUS : float = 12
ROCK_X : float = PLAYER_X
ROCK_Y : float = LINE_Y - PLAYER_HEIGHT + PLAYER_HEIGHT/4
GRAVITY = 0.5

class Rock:

    def __init__(self, game_window : display) -> None:
        self.cordX = ROCK_X
        self.cordY = ROCK_Y
        self.radius = ROCK_RADIUS
        self.window = game_window
        self.isThrowing = False
        self.velocity = [0,0]
        self.bounces = 0
        self.bounce_factor = 0.9
        self.onGround = False

    def show(self) -> None:
        rock_img = draw.circle(self.window, BLACK, (self.cordX, self.cordY), self.radius)

    
    def throw(self, power, angle) -> None:
        self.velocity[0] = -power * math.cos(math.radians(angle))
        self.velocity[1] = -power * math.sin(math.radians(angle))

    def update(self, wall) -> None:
        self.velocity[1] += GRAVITY
        self.cordX += self.velocity[0]
        self.cordY += self.velocity[1]

        if self.cordY > LINE_Y-self.radius and self.cordY < LINE_Y-self.radius+1:
            self.onGround = True
        else:
            self.onGround = False

        if self.cordY + self.radius >= LINE_Y:
            self.cordY = LINE_Y - self.radius
            self.velocity[1] = -self.velocity[1] * self.bounce_factor
            self.velocity[0] *= 0.8
            if not self.onGround:
                self.bounces += 1

        if wall.collideRight(self):
            self.velocity[1] = -self.velocity[1] * self.bounce_factor
            self.velocity[0] *= 0.7

            if self.cordX - self.radius < wall.cordX:
                self.cordX = wall.cordX - self.radius
                if self.velocity[0] > 0:  # Rock is moving to the right
                    self.velocity[0] *= -1  # Reverse horizontal velocity
                    
            else:
                self.cordX = wall.cordX + GOAL_WIDTH + self.radius
                if self.velocity[0] < 0:  # Rock is moving to the left
                    self.velocity[0] *= -1
            self.velocity[1] *= -1

    def reset(self):
        self.cordX = ROCK_X
        self.cordY = ROCK_Y
        self.isThrowing = False
        self.velocity = [0,0]
        self.onGround = False
        self.bounces = 0

    def collideGoal(self, goal):
        if (self.cordX > goal.cordX+20 and self.cordX < goal.cordX + GOAL_WIDTH and
                self.cordY - self.radius > goal.cordY and self.cordY < goal.cordY + GOAL_HEIGHT):
            return True
        return False
    
    
