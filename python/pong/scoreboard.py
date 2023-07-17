from turtle import Turtle


def create_board(x, y):
    board = Turtle()
    board.ht()
    board.goto(x=x, y=y)
    board.color('white')

    return board


class Scoreboard:

    def __init__(self, screen_height, screen_width):
        self.screen_height = screen_height / 2
        self.screen_width = screen_width / 2
        self.board_left = create_board(-self.screen_width / 2, self.screen_height - 60)
        self.board_right = create_board(self.screen_width / 2, self.screen_height - 60)
        self.score_left = 0
        self.score_right = 0

    def add_score(self, direction):
        if direction == 'left':
            self.score_left += 1
            self.board_left.clear()
            self.board_left.write(self.score_left, align='center', font=('Arial', 32, 'normal'))
        elif direction == 'right':
            self.score_right += 1
            self.board_right.clear()
            self.board_right.write(self.score_right, align='center', font=('Arial', 32, 'normal'))

