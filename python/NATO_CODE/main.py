#TODO 1. Create a dictionary in this format:

import pandas as pd
import time

file_path = "./nato_phonetic_alphabet.csv"
data = pd.read_csv(file_path)
itr = data.iterrows()
# iterrows returns data in the form of <index>.<column>
my_dict = {row_data.letter : row_data.code for index, row_data in itr}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# while True:
#     try:
#         prompt = input("What's the word you have?").upper()
#         code = [my_dict[letter] for letter in prompt]
#     except KeyError as key:
#         print(f"Sorry. {key} is not a valid input.")
#     else:
#         print(code)

def generate_phonetic():
    inp = "123"  # Fixed value to mock input
    try:
        output_list = [my_dict[letter] for letter in inp]
    except KeyError:
        generate_phonetic()
    else:
        print(output_list)


before = time.time()
try:
    generate_phonetic()
except RecursionError:
    after = time.time()
    print(f"This took just {round(after - before, 3)} seconds to crash!")

