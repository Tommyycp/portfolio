from game_data import data
import random
from art import logo, vs
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0
end_prompt = False

def celebrity_generator():
    index = random.randint(0, len(data) - 1)
    return data[index]

dict_b = celebrity_generator()


while not end_prompt:
    dict_a = dict_b
    dict_b = celebrity_generator()

    while dict_a == dict_b:
        dict_a = celebrity_generator()
    a_followers = dict_a['follower_count']
    b_followers = dict_b['follower_count']

    cls()
    print(logo)
    print(
        f"Compare A {dict_a['name']}, {dict_a['country']}, {dict_a['description']}")

    print(vs)

    print(
        f"Compare B {dict_b['name']}, {dict_b['country']}, {dict_b['description']}")
    
    if score > 0:
        print(f"You're right! Current score: {score}")
    comparsion_prompt = input(
        "Who has more followers? Type 'A' or 'B'.").lower()
    if a_followers > b_followers and comparsion_prompt == 'a':
        score += 1
    elif b_followers > a_followers and comparsion_prompt == 'b':
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        end_prompt = True
        print(f"Sorry, that's wrong. Final Score: {score}.")