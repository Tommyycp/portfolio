from turtle import Turtle
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake:

    def __init__(self, length, screen_width, screen_height):
        self.snakes_dict = self.create_snakes(length)
        self.snake_head = self.snakes_dict[0]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_head.color("cyan")

    def create_snakes(self, length):
        turtles = {}
        starting_x = 0
        for i in range(length):
            tur = Turtle(shape='square')
            tur.up()
            tur.setx(starting_x)
            tur.color('white')
            turtles[i] = tur
            starting_x -= 20
        return turtles

    def move(self):
        # Move the last elements up one point
        for j in range(len(self.snakes_dict) - 1, 0, -1):
            # Iterating the index backwords
            # Len function returns the total number of elements. However, the index starts counting from 0.
            # Therefore, minus 1 whenever we anticiapte the index.
            # Because the dictionary key does not have -1.
            # Because if -1 is included, the top head will equals to the tail head
            # Therefore, we stop the range operation at 0
            next_turtle_x = self.snakes_dict[j - 1].xcor()
            next_turtle_y = self.snakes_dict[j - 1].ycor()
            self.snakes_dict[j].goto(next_turtle_x, next_turtle_y)
            # Last coor == second to last coor
            # second to last coor == third to last x__coor
            # ....
            # second coor == first_coor
            # Notice how the first_coor is not 'moved up'.
        self.snake_head.fd(20)

    def add_snake(self):
        new_tur = Turtle(shape="square")
        new_tur.up()
        new_tur.color('white')
        self.snakes_dict[len(self.snakes_dict)] = new_tur

    def self_bite(self):
        past_coor = []
        for snake in range(1, len(self.snakes_dict)):
            inst = self.snakes_dict[snake]
            past_coor.append((inst.pos()))
        for c in past_coor:
            x = c[0]
            y = c[1]
            if x - 0.5 <= self.snake_head.xcor() <= x + 0.5:
                if y - 0.5 <= self.snake_head.ycor() <= y + 0.5:
                    return True
        return False

    def is_snake_out_of_bounds(self):
        max_width = self.screen_width / 2 - 15
        max_height = self.screen_height / 2 - 15
        if -max_width <= self.snake_head.xcor() <= max_width and -max_height <= self.snake_head.ycor() <= max_height:
            return False
        return True

    def is_snake_on_cake(self, x, y):
        if x - 20 <= self.snake_head.xcor() <= x + 20 and y - 20 <= self.snake_head.ycor() <= y + 20:
            return True
        return False

    def east(self):
        if not self.snake_head.heading() == WEST:
            self.snake_head.seth(EAST)

    def north(self):
        if not self.snake_head.heading() == SOUTH:
            self.snake_head.seth(NORTH)

    def west(self):
        if not self.snake_head.heading() == EAST:
            self.snake_head.seth(WEST)

    def south(self):
        if not self.snake_head.heading() == NORTH:
            self.snake_head.seth(SOUTH)
