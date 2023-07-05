import random
import art

def backjack():
  print (art.logo)
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  user_cards = random.choices(cards, k=2)
  computer_cards = random.choices(cards, k=2)
  print (f"Your cards: {user_cards}, current score: {sum(user_cards)}")
  print (f"Computer's first card: {computer_cards[0]}")
  continue_prompt = True
  while continue_prompt:
    continue_prompt = input("Type y to get another cards, type 'n' to pass.")
    if continue_prompt == "y":
      if sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
      user_cards.append(random.choice(cards))
      if sum(user_cards) > 21 and 11 in user_cards:
        user_cards[user_cards.index(11)] = 1
      if sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards[computer_cards.index(11)] = 1
        
    print (f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print (f"Computer's first card: {computer_cards[0]}")
      
    if sum(user_cards) > 21 or sum(computer_cards) > 21 or continue_prompt == "n":
      continue_prompt = False
      print (f"Game Over\nYour final hand: {user_cards},final score: {sum(user_cards)}\nComputer's final hand: {computer_cards},final score: {sum(computer_cards)}")
      if sum(user_cards) == sum(computer_cards):
        print ("It's a draw")
      elif sum(computer_cards) == 21:
        print ("Computer wins")
      elif sum(user_cards) > 21 and sum(computer_cards) < 21:
        print ("Computer wins.")
      elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) < 21:
        print ("Computer wins.")
      elif sum(computer_cards) < sum(user_cards) and sum(computer_cards) > 21:
        print ("Computer wins")
      else:
        print ("You win")
      restart = input("Do you want to start over, 'y' or 'n'?")
      if restart == "y":
        print("\033[H\033[J", end="")
        backjack()
      else:
        print ("See You!")

start_prompt = input("Do you want to start the game, y or n?")
if start_prompt == "y":
  print("\033[H\033[J", end="")
  backjack()
