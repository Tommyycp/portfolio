# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

i = random.randint(0,len(names)-1)
# change len into index, don't forget to minus one.

print (f"{names[i]} is going to buy the meal today!")

# Alternative method 

print (f"{random.choice(names)} will pay the bill.")

# Use random.choice(list) to achieve the target of retrieving a particular items from the list. 
