MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0
}

currency = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if (choice == "off"):
        break
    elif (choice == "report"):
        for key in resources:
            print(f"{key}: {resources[key]}")
    else:
        print("Please Enter coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        
        amount = quarters*currency["quarter"] + dimes*currency["dime"] + nickels*currency["nickel"] + pennies*currency["penny"]

        if (resources["water"] < MENU[choice]["ingredients"]["water"]):
            print("Sorry there is not enough water")
            continue
        
        if (resources["milk"] < MENU[choice]["ingredients"]["milk"]):
            print("Sorry there is not enough water")
            continue
        
        if (resources["milk"] < MENU[choice]["ingredients"]["milk"]):
            print("Sorry there is not enough water")
            continue

        if amount < MENU[choice]["cost"]:
            print("Sorry thats not enough money")
        
        price = MENU[choice]["cost"]

        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]

        resources["money"] += price

        if (price < amount):
            print(f"Here is your change! {amount-price}")