print("Welcome to Rock Paper Scissor Shot!")

rock = '''

ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

PAPER!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

SCISSORS!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

computer_choice = random.randint(0,2)

print (f"Your choice is\n{list[user_choice]}")
print (f"Computer choice is \n{list[computer_choice]}")

# matrix 1 == rock -- rock; rock -- paper; rock -- scissors
# matrix 2 == paper -- rock; paper -- paper; paper -- scissors;
# matrix 3 == scissor -- rock; scissor -- paper; scissors -- scissors
matrix = [["Draw", "Lose", "Win"],["Win", "Draw", "Lose"],["Lose", "Win", "Draw"]]

# I choose rock == matrix[0]
# I choose paper == matrix[1]
# I choose scissors == matrix[2]

# I choose rock, computer chooses rock == matrix[0][0]
# I choose rock, computer chooses paper == matrix[0][1]
# I choose rock, computer chooses scissors == matrix[0][2]
# ...

print(matrix[user_choice][computer_choice])
