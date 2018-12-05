from settings import *
from objects import Board, Pong
from display import Bar, Score
import sys


class Game:

    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

        self.change = 0

        self.player_score = 0
        self.opponent_score = 0
        self.player_board = Board(self.screen, 'left')
        self.opponent_board = Board(self.screen, 'right')
        self.pong = Pong(self.screen, self.player_board, self.opponent_board)

        self.top_bar = Bar(self.screen, 'top')
        self.bottom_bar = Bar(self.screen, 'bottom')

        self.left_score = Score(self.screen, str(self.player_score), 'left')
        self.right_score = Score(self.screen, str(self.opponent_score), 'right')

    def new(self):
        self.run()

    def run(self):
        self.playing = True
        self.screen.fill(WHITE)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updates()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == UP:
                    self.change = -1
                elif event.key == DOWN:
                    self.change = 1
                elif event.key == Q:
                    print(self.pong.velocity, self.pong.cy)
                elif event.key == W:
                    self.pong.random_angle()
            if event.type == pg.KEYUP:
                if event.key == DOWN or event.key == UP:
                    self.change = 0

    def updates(self):
        self.player_board.move(self.change)
        self.pong.move()
        if self.pong.y <= HEIGHT - BAR_WIDTH - self.player_board.height + 2:
            self.opponent_board.y = self.pong.y
        if self.pong.point() == 0:
            self.opponent_score += 1
            self.pong = Pong(self.screen, self.player_board, self.opponent_board)
        elif self.pong.point() == 1:
            self.player_score += 1
            self.pong = Pong(self.screen, self.player_board, self.opponent_board, neg=-1)
        self.left_score.update(str(self.player_score))
        self.right_score.update(str(self.opponent_score))

    def draw(self):
        self.screen.fill(BLACK)
        self.player_board.display()
        self.opponent_board.display()
        self.pong.display()
        self.top_bar.display()
        self.bottom_bar.display()
        self.left_score.display()
        self.right_score.display()
        pg.display.update()


g = Game()
while g.running:
    g.new()

pg.quit()
