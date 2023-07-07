MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

res = {
    'water': 500,
    'milk': 500,
    'coffee': 100,
    'money': 0,
}


def is_insufficient(drink):
    required_ingredients = (MENU[drink]['ingredients'])
    for ingredient in required_ingredients:
        if res[ingredient] < required_ingredients[ingredient]:
            return True
    return False


def coins_insertion():
    q = int(input('How many quarters do you have?')) * 0.25
    d = int(input('How many dimes do you have?')) * 0.1
    n = int(input('How many nickels do you have?')) * 0.05
    p = int(input('How many pennies do you have?')) * 0.01
    return q + d + n + p


def transaction(selected_drink):
    if selected_drink == 'report':
        print(res)
    else:
        payment = coins_insertion()
        if is_insufficient(selected_drink):
            print(f"Sorry, not enough resources. {payment} refunded.")
        elif payment < MENU[selected_drink]['cost']:
            print(f"Sorry, not enough money. {payment} refunded")
        else:
            res['money'] += MENU[selected_drink]['cost']
            change = payment - MENU[selected_drink]['cost']
            for i in (MENU[selected_drink]['ingredients']):
                res[i] -= MENU[selected_drink]['ingredients'][i]
            print(f"Here you go! {selected_drink}")
            if change > 0:
                print(f"Don't forget your change: {change}")


while True:
    user_prompt = input("What would you like? (espresso/latte/cappuccino)?").lower()
    if user_prompt == 'off':
        print("System closed")
        break
    else:
        print(user_prompt not in MENU)
        print(user_prompt != 'report')
        while user_prompt not in MENU or user_prompt != 'report':
            print(f"{user_prompt} not found in menu. Please order again.")
            user_prompt = input("What would you like? (espresso/latte/cappuccino)?").lower()
        else:
            transaction(user_prompt)
