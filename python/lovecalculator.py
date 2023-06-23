print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

tn = name1.lower() + name2.lower()

t1 = tn.count("t") + tn.count("r")+ tn.count("u")+ tn.count("e")
t2 = tn.count("l") + tn.count("o")+ tn.count("v")+ tn.count("e")
score = int(str(t1)+str(t2))

if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print (f"Your score is {score}, you are alright.")
else:
    print(f"Your score is {score}.")

