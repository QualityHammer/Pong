from settings import *

pg.init()
pg.font.init()


class Score:

    font = pg.font.SysFont('Impact', 35)

    def __init__(self, screen, num, side):
        self.screen = screen
        self.num = num

        self.surf = Score.font.render(num, False, BLACK)
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()
        if side == 'left':
            self.x = 0
        else:
            self.x = WIDTH - self.width
        self.y = 0

    def update(self, num):
        self.num = num
        self.width = self.surf.get_width()
        self.surf = Score.font.render(num, False, BLACK)

    def display(self):
        self.screen.blit(self.surf, (self.x, self.y))


class Bar:

    def __init__(self, screen, side):
        self.screen = screen
        self.width = WIDTH
        self.height = BAR_WIDTH
        if side == 'top':
            self.y = 0
        else:
            self.y = HEIGHT - self.height
        self.x = 0

    def display(self):
        pg.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))
