import random
import hangman_art
import hangman_words

print(hangman_art.logo + "\n")

word_list = hangman_words.word_list
stages = hangman_art.stages

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(f'Pssst, the solution is {chosen_word}.')

display = []
display[:0] = "_"*len(chosen_word)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print (f"\nThe letter {guess} is already there. \n{' '.join(display)} \nYou still have {lives} chance(s) left.\n")
    else:       
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"{' '.join(display)}")
        if guess not in chosen_word:
             lives -= 1
             if lives == 0:
                 end_of_game = True
                 print ("You've used all the chances! You lose")
             else:
                 print (f"\n{stages[lives]}\n The letter {guess} is NOT in the word. You still have {lives} chance(s) left.\n")
        if "_" not in display:
            end_of_game = True
            print ("You win! Congratulations!")
