from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self, screen_width, screen_height, level):
        self.screen_width = int(screen_width / 2)
        self.screen_height = int(screen_height / 2)
        self.move_distance = STARTING_MOVE_DISTANCE + int(level)*MOVE_INCREMENT
        self.cars = []
        self.create()

    def create(self):
        car = Turtle(shape='square')
        car.up()
        car.speed('fastest')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(r.choice(COLORS))
        car.seth(180)
        car.goto(x=self.screen_width, y=r.randint(-self.screen_height + 100, self.screen_height -100))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.fd(r.randint(0, self.move_distance))

    def is_crash(self, player):
        for car in self.cars:
            # if player.distance(car.pos()) < 21:
            x_dis = player.xcor() - car.xcor()
            y_dis = player.ycor() - car.ycor()
            if abs(x_dis) < 30 and abs(y_dis) < 25:
                return True
        return False

    def clear_cars(self):
        self.cars.clear()

