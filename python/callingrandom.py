import random

def num_guess ():
  num = random.randint(1,100)
  attempts = 0
  attempts_prompt = input("Difficulty level, easy or hard?\n").lower()
  if attempts_prompt == "easy":
    attempts = 10
  elif attempts_prompt == 'hard':
    attempts = 5   
  end_game = False
  print("\033[H\033[J", end="")
  while not end_game:
    if attempts == 0:
      end_game = True
      print (f"You've used up all chances! The number is {num}.")
    else:
      print (f"You still have {attempts} chances remaining")
      num_user = int(input("Guess a number\n"))
      if num_user < num:
        print ("Too low")
        attempts -= 1
      elif num_user > num:
        print ("Too high")
        attempts -= 1
      else:
        end_game = True
        print ('Jackpot')    
  if end_game == True:
    restart_prompt = input("Do you wanna try again, yes or no?\n").lower()
    if restart_prompt == "yes" or restart_prompt == "y" :
      print("\033[H\033[J", end="")
      num_guess ()
    else:
      print ("Bye")
start_prompt = input ("Type 'y' to start the game\n").lower()
if start_prompt == 'y':
  num_guess ()
