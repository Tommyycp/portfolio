alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z']

def caesar(mode, string, number):
    final = ''
    if mode == "encode":
        for i, v in enumerate(string):
            if v not in alphabet:
                final += v
            else:
                index_alphabet = alphabet.index(v) + number
                if index_alphabet > len(alphabet) - 1:
                    index_alphabet = index_alphabet % len(alphabet)
                final += alphabet[index_alphabet]
    elif mode == "decode":
        for i, v in enumerate(string):                
            if v not in alphabet:
                final += v
            elif number > 26:
                index_alphabet = alphabet.index(v) - number % len(alphabet)
                final += alphabet[index_alphabet]
            else:
                index_alphabet = alphabet.index(v) - number
                final += alphabet[index_alphabet]

    print(f"The {mode}d text is {final}")

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(mode=direction, string=text, number=shift)
    ask = input("Would you like to run again, yes or no?").lower()
    if ask == 'no':
        end = True
        print ("Goodbye, hope you enjoy the program!\n")