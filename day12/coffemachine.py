menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def resource_check(orderingredients):
    for item in orderingredients:
        if resources[item] < orderingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Insert coins:")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def money_enough(menucost, money):
    if money >= menucost:
        global profit
        profit += menucost
        change = round(money - menucost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_drink(drink, orderingredients):
    for item in orderingredients:
        resources[item] -= orderingredients[item]
    print(f"Your {drink} is ready.")

# Main loop
loop = True

while loop:
    prompt = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    
    if prompt == 'off':
        loop = False
        
    elif prompt == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
        
    elif prompt in menu:
        drink = prompt
        drinkdict = menu[drink]
        if resource_check(drinkdict["ingredients"]):
            money = process_coins()
            if money_enough(drinkdict['cost'], money):
                make_drink(drink, drinkdict["ingredients"])
