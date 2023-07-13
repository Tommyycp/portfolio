import random as r
import turtle as t

t.colormode(255)

def random_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    return (red, green, blue)

tommy = t.Turtle()
degree = 360
tommy.up()
tommy.sety(100)
tommy.pd()
tommy.speed(0)

angle = 0
while angle <= 360:
    tommy.pencolor(random_color())
    tommy.circle(150)
    tommy.rt(2)
    angle += 2

screen = t.Screen()
screen.title("Welcome to Tommy's Turtle Kingdom!")
screen.exitonclick()
