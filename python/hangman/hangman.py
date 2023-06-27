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

display = []
display[:0] = "_"*len(chosen_word)
guessed_words = []

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print (f"\nThe letter {guess} is already there. \n{' '.join(display)} \nYou still have {lives} chance(s) left.\n")
    elif guess in guessed_words:
        print (f"You have already guessed the letter {guess}.\nAnd it is not in the word.")
    elif guess == chosen_word:
        end_of_gane = True
        print ("GENUIUS!")
    else:       
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"{' '.join(display)}")
        if guess not in chosen_word:
             lives -= 1
             guessed_words.append(guess)
             if lives == 0:
                 end_of_game = True
                 print (f"You've used all the chances! You lose. The word is {chosen_word}.")
             else:
                 print (f"\n{stages[lives]}\n The letter {guess} is NOT in the word. You still have {lives} chance(s) left.\n")
        if "_" not in display:
            end_of_game = True
            print ("You win! Congratulations!")
