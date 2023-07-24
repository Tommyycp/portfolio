# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_pathname = './Input/Letters/starting_letter.txt'
name_pathname = './Input/Names/invited_names.txt'
output_folder = './Output/ReadyToSend/'

with open(name_pathname, mode='r') as file:
    name_list = file.read().splitlines()

with open(letter_pathname, mode='r') as file:
    sample_letter = file.read()

for i in name_list:
    file_name = f"./Output/ReadyToSend/Letter_to_{i}.txt"
    with open(file_name, mode='w') as new_file:
        new_file.write(sample_letter.replace("[name]", f"{i}"))