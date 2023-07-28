#TODO 1. Create a dictionary in this format:

import pandas as pd

file_path = "./nato_phonetic_alphabet.csv"
data = pd.read_csv(file_path)
itr = data.iterrows()
my_dict = {row_data.letter:row_data.code for index,row_data in itr}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# prompt = input("What's the word you have?")
