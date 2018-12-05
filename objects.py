from settings import *
import random as rand


class Pong:

    def __init__(self, screen, lboard, rboard, neg=1, diameter=10):
        self.lboard = lboard
        self.rboard = rboard
        self.screen = screen
        self.diameter = diameter
        self.velocity = 15 * neg

        self.x = WIDTH / 2
        self.y = HEIGHT / 2

        self.startx = self.x
        self.starty = self.y
        num = rand.uniform(0.5, 1.0)
        neg = rand.randint(0, 1)
        if neg == 0:
            self.cy = num
        else:
            self.cy = num * -1

    def random_angle(self):
        self.cy = rand.uniform(-1.0, 1.0)

    def point(self):
        if self.x < 0:
            return 0
        elif self.x + self.diameter > WIDTH:
            return 1

    def move(self):
        self.x += self.velocity
        self.y += self.cy * self.velocity
        if self.y <= BAR_WIDTH or self.y + self.diameter >= HEIGHT - BAR_WIDTH:
            self.bounce()
        elif self.x <= self.lboard.width:
            if self.lboard.y <= self.y <= self.lboard.y + self.lboard.height \
                    or self.lboard.y <= self.y + self.diameter <= self.lboard.y + self.lboard.height:
                self.bounce(wall=False)
        elif self.x + self.diameter >= WIDTH - self.rboard.width:
            if self.rboard.y <= self.y <= self.rboard.y + self.rboard.height \
                    or self.rboard.y <= self.y + self.diameter <= self.rboard.y + self.rboard.height:
                self.bounce(wall=False)

    def bounce(self, wall=True):
        self.cy = -self.cy
        if not wall:
            self.velocity = -self.velocity

    def flip(self):
        self.velocity = -self.velocity

    def display(self):
        pg.draw.rect(self.screen, WHITE, (self.x, self.y, self.diameter, self.diameter))


class Board:

    color = WHITE
    velocity = 10

    def __init__(self, screen, side):
        self.screen = screen
        self.width = 20
        self.height = 100
        if side == 'left':
            self.x = 0
        else:
            self.x = WIDTH - self.width
        self.y = 100
        self.bottom = self.y + self.height

    def display(self):
        pg.draw.rect(self.screen, Board.color, (self.x, self.y, self.width, self.height))

    def move(self, neg):
        self.y += neg * Board.velocity
        if self.y < BAR_WIDTH:
            self.y = BAR_WIDTH
        elif self.y + self.height > HEIGHT - BAR_WIDTH:
            self.y = HEIGHT - BAR_WIDTH - self.height

