# Add
def add (a,b):
  return a + b

def substract (a,b):
  return a - b

def multiply (a, b):
  return a * b

def divide (a,b):
  return a/b

operators = {
  "+": add,
  "-": substract, 
  "*":multiply, 
  "/":divide,
}

def calculator():
  end = False
  num1 = float(input("What is the first number?\n"))
  print(' '.join(list(operators.keys())))
  symbol = input("Pick an operation from the line above\n")
  num2 = float(input("What is the second number?\n"))
  answer = operators[symbol](num1,num2)
  print(f'{num1} {symbol} {num2} equals to {answer}')
  
  while not end:
    prompt = input(f"Take 'y' to continue conculating with {answer}, type 'n' to start a new calculation, type 'exit' to exit the program.\n").lower()
    if prompt == "n\n":
      end = True
      calculator()
    elif prompt == "exit":
      end = True
      print ("See You!")
    else:
      print (' '.join(list(operators.keys())))
      symbol = float("Pick another operation from the line above\n")
      num3 = float(input("What is number?\n"))
      answer_old = answer
      answer = operators[symbol](answer,num3)
      print (f'{answer_old} {symbol} {num3} equals to {answer}')

calculator()
