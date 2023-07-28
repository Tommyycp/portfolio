import turtle
import pandas as pd

screen = turtle.Screen()
screen.title = "Guess The State"
map = './blank_states_img.gif'
screen.bgpic(map)

data_path = './50_states.csv'
data = pd.read_csv(data_path)
states_list = data['state']

FONT = ("Arial", 12, 'bold')
guessed = []
total_count = states_list.shape[0]

while len(guessed) < total_count:
    answer = screen.textinput(title=f"{len(guessed)}/{total_count}", prompt="Write down any states you know.")
    if answer == 'exit':
        break
    else:
        for state_name in states_list:
            if state_name.lower() == answer.lower():
                row = data[data.state == state_name]
                x_co = row.iloc[0].x
                y_co = row.iloc[0].y
                tur = turtle.Turtle()
                tur.ht()
                tur.penup()
                tur.goto(x_co, y_co)
                tur.write(f"{state_name}", align='center', font=FONT)
                guessed.append(state_name)
                break

complete_list = states_list.to_list()
ungussed = [country for country in complete_list if country not in guessed]

complete_list = pd.DataFrame(ungussed, columns=['State Name'])
complete_list.to_csv('./not_guessed.csv')
