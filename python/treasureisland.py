print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

s1 = input("Left or right?").lower()
if s1 == "left":
  s2 = input("Congratulation! Next round. \nswim or wait?").lower()
  if s2 == "wait":
    s3 = input("Congratulation! Next round.\nWhich door, red, blue, or yellow?").lower()
    if s3 == "red":
      print ("Burned by fire. Game Over.")
    elif s3 == "blue":
      print ("Eaten by Beast. Game Over.")
    elif s3 == "yellow":
      print ("You win!")
    else:
      print("Game Over")
  else:
    print ("Game Over")
else:
  print ("Game Over")

