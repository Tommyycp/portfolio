from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(width=1000, height=1000)
colors = ['green', 'blue', 'pink', 'black', 'brown', 'purple', 'red', 'orange', 'yellow', ]

turtles = {}
place = 1

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    turtles[colors[i]] = new_turtle

y = -350
for turtle in turtles:
    tur = turtles[turtle]
    tur.penup()
    tur.goto(-500, y)
    y += 50

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet",
                                prompt="Type again. Which turtle will win the race? Enter a color: ")

is_race_on = True
while is_race_on:
    for turtle in turtles:
        tur = turtles[turtle]
        steps = r.randint(0, 10)
        tur.fd(steps)
        if tur.xcor() > 470:
            winner = turtle
            is_race_on = False
            break
if winner == user_bet:
    print("You win")
    print(f"Winner is {winner}.")
else:
    print("You lose")
    print(f"Winner is {winner}.")


screen.exitonclick()

# Explain why this double-for-loop doesn't work
# for turtle in turtle_list:
#     for y in range(-180, 180, 50):
#         turtle.goto(-240,y)

# For-loop priority starts from the innermost loop
# y = (-180, -130, -80, ...)
# object_1 turtle.goto (-240.-180), (-240,-130)...
# object_2 turtle.goto (-240,-180), (-240, -130)...
# In the end, all turtle_instances will end up with the same place
