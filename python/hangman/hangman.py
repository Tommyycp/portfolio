letters = ['a', 'b', 'c', 'd', 'e']

start_1 = letters[0]
start_2 = letters[1]

for i in range(2, len(letters)):
    current = letters[i]
    print(start_1, start_2, current)
    start_1 = start_2
    start_2 = current
