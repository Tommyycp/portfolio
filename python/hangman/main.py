from hangman import HangMan

words = []
stop = 0
while True:
    prompt = input("Give me a list of words.").lower()
    if prompt == "stop" or prompt == "off":
        break
    else:
        words.append(prompt)

h = HangMan(words)
h.game_on()
