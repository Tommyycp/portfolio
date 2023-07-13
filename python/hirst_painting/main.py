import colorgram
import turtle as t
import random as r


def get_color(path, number):
    palette = colorgram.extract(path, number)
    color_list = []
    for i in palette:
        values = (i.rgb.r, i.rgb.g, i.rgb.g)
        color_list.append(values)
    return color_list


colors = [(240, 74, 74), (8, 147, 147), (222, 170, 170), (181, 160, 160), (26, 126, 126), (43, 192, 192),
          (250, 221, 221), (84, 24, 24), (125, 193, 193), (31, 169, 169), (185, 35, 35), (253, 223, 223), (211, 63, 63),
          (24, 183, 183), (168, 21, 21), (212, 130, 130), (242, 161, 161), (4, 111, 111), (246, 166, 166)]

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()
screen.setworldcoordinates(0, 0, 450, 450)
turtle.penup()

for y in range(0, 451, 50):
    for x in range(0, 451, 50):
        turtle.goto(x, y)
        turtle.dot(20,r.choice(colors))

screen.exitonclick()
