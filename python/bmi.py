h = float(input("enter your height in m: "))
w = float(input("enter your weight in kg: "))

b = round(w/h**2)
# round BMI number


if b < 18.5:
    print (f"Your BMI is {b}, you are underweight.")
elif b < 25:
    print (f"Your BMI is {b}, you have a normal weight.")
elif b < 30:
    print(f"Your BMI is {b}, you are slightly overweight.")
elif b <35:
    print(f"Your BMI is {b}, you are obese.")
elif b > 35:
    print (f"Your BMI is {b}, you're clinically obese.")