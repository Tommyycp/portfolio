from turtle import Turtle, Screen

FONT = ('Times News Roman', 18, 'normal')


def get_highest():
    with open("./highest_score.txt") as file:
        score = file.read()
        score = int(score)
        return score


def write_highest(score):
    with open("./highest_score.txt", mode='w') as file:
        file.write(f"{score}")


class ScoreBoard(Turtle):

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width / 2
        self.screen_height = screen_height / 2
        self.score = 0
        self.highest_score = get_highest()
        super().__init__()
        self.up()
        self.shapesize(10, 10, 10)
        self.ht()
        self.color('white')
        self.goto(x=0, y=self.screen_height - 75)

    def update(self):
        self.clear()
        self.write(f"Current:{self.score}, Highest: {self.highest_score}", False, align='center', font=FONT)

    def add(self):
        self.score += 1
        if self.score > self.highest_score:
            self.highest_score = self.score
            write_highest(self.highest_score)
        self.update()

    def reset(self):
        self.score = 0
        self.clear()