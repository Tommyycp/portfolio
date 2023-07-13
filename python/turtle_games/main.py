import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def fd():
    turtle.fd(25)


def bk():
    turtle.bk(25)


def rt():
    new = turtle.heading() - 10
    turtle.seth(new)

def lt():
    new = turtle.heading() +10
    turtle.seth(new)

def cls():
    turtle.up()
    turtle.home()
    turtle.clear()
    turtle.pd()

screen.listen()
screen.onkey(fd, "w")
screen.onkey(bk, "s")
screen.onkey(lt, "a")
screen.onkey(rt, "d")
screen.onkey(cls, "c")

screen.exitonclick()
