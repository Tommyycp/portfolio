from turtle import Turtle

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:

    def __init__(self, length, screen_width, screen_height):
        self.length = length
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snakes = []
        self.create_snakes()
        self.snake_head = self.snakes[0]

    def create_snakes(self):
        starting_x = 0
        for i in range(self.length):
            snake = Turtle(shape='square')
            snake.up()
            snake.setx(starting_x)
            snake.color('white')
            starting_x -= 20
            self.snakes.append(snake)


    def move(self):
        # Move the last elements up one point
        for j in range(len(self.snakes) - 1, 0, -1):
            # Iterating the index backwards
            # Len function returns the total number of elements. However, the index starts counting from 0.
            # Therefore, minus 1 whenever we anticiapte the index.
            # Because the dictionary key does not have -1.
            # Because if -1 is included, the top head will equals to the tail head
            # Therefore, we stop the range operation at 0
            next_turtle_x = self.snakes[j - 1].xcor()
            next_turtle_y = self.snakes[j - 1].ycor()
            self.snakes[j].goto(next_turtle_x, next_turtle_y)
            # Last coor == second to last coor
            # second to last coor == third to last x__coor
            # ....
            # second coor == first_coor
            # Notice how the first_coor is not 'moved up'.
        self.snake_head.fd(20)

    def add_snake(self):
        snake = Turtle()
        snake.shape('square')
        snake.up()
        snake.color('white')
        self.snakes.append(snake)

    def self_bite(self):
        for snake in self.snakes[1:]:
            if self.snake_head.distance(snake) < 1:
                return True
        return False

    def is_snake_out_of_bounds(self):
        max_width = self.screen_width / 2 - 15
        max_height = self.screen_height / 2 - 15
        if -max_width <= self.snake_head.xcor() <= max_width and -max_height <= self.snake_head.ycor() <= max_height:
            return False
        return True

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
