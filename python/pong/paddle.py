from turtle import Turtle

LENGTH = 10


def create_paddle(x):
    y_cor = 0
    paddle = []
    for _ in range(LENGTH):
        paddle_block = Turtle(shape='square')
        paddle_block.up()
        paddle_block.color('white')
        paddle_block.speed('fastest')
        paddle_block.goto(x=x, y=y_cor)
        paddle.append(paddle_block)
        y_cor -= 20
    return paddle


# def move_paddle(paddle_list, heading, limit):
#     for i in paddle_list:
#         if 0 < limit < i.ycor():
#             break
#         elif limit < 0 and i.ycor() < limit:
#             break
#         else:
#             i.seth(heading)
#             i.fd(40)


class Paddle:

    def __init__(self, screen_width, screen_length):
        self.length = screen_length / 2 - 20
        self.width = screen_width / 2 - 20
        self.left_paddle = create_paddle(-self.width)
        self.right_paddle = create_paddle(self.width)

    # def is_out_of_bound(self, paddle_list):
    #     for i in paddle_list:
    #         if not -self.width+20 < i.ycor() < self.width+20:
    #             return True
    #     return False

    def move_paddle(self, paddle_list, heading):
        for i in paddle_list:
            i.seth(heading)
            i.fd(40)

    def left_paddle_up(self):
        # if not self.is_out_of_bound(self.left_paddle):
        self.move_paddle(self.left_paddle, 90)

    def right_paddle_up(self):
        # if not self.is_out_of_bound(self.right_paddle):
        self.move_paddle(self.right_paddle, 90)

    def left_paddle_down(self):
        # if not self.is_out_of_bound(self.left_paddle):
        self.move_paddle(self.left_paddle, 270)

    def right_paddle_down(self):
        # if not self.is_out_of_bound(self.right_paddle):
        self.move_paddle(self.right_paddle, 270)
