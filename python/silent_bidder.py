bidding = {}
def add_bidder (name, amount):
  bidding [name] = amount

end = False
while not end:
  bidder_name = input("What's your name?\n")
  bid_amount = int(input("What is your bid?\n"))
  other_bidders = input("Are there any other bidders,   yes or no?").lower()
  add_bidder (name=bidder_name, amount= bid_amount)
  if other_bidders == "no":
    end = True
    for key in bidding:
      initial = 0
      if bidding[key] > initial:
        initial = bidding[key]
    max = list(bidding.keys())[list(bidding.values()).index(initial)]
    print (f"{max} gets the bid with {initial}")
  else:
    clear()
