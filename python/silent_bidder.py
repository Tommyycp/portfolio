bidding = {}
def add_bidder (name, amount):
  bidding [name] = amount

end = False
dulplicate_number = 1
dulplicate_bidder = []

while not end:
  bidder_name = input("What's your name?\n")
  bid_amount = int(input("What is your bid?\n"))
  if bidder_name in bidding:
    ans = input(("Are you sure you haven't bid before?")).lower()
    if ans == "yes":
      for key in bidding:
        if key in bidder_name:
          dulplicate_number += 1
      bidder_name += f"_{dulplicate_number}"   
      print (f"Your name is {bidder_name}")
    else:
      print("\033[H\033[J", end="")
      continue
  elif bid_amount in list(bidding.values()):
    print ("Someone else bid the same amount as you. Please raise the bid.")
    continue

  add_bidder (name=bidder_name, amount= bid_amount)

  other_bidders = input("Are there any other bidders,   yes or no?").lower()
  if other_bidders == "no":
    end = True
    max_index = max(list(bidding.values()))
    max_key = list(bidding.keys())[list(bidding.values()).index(max_index)]
    print (f"{max_key} gets the bid with ${max_index}")
  else:
    print("\033[H\033[J", end="")
