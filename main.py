MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk':0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(choice):
    for item in resources:
        if resources[item] > MENU[choice]['ingredients'][item]:
            return True
    print(f"Sorry, we don't have enough {item}")


def make_coffee():
    for item in resources:
        resources[item] -= MENU[choice]['ingredients'][item]
        change = total - MENU[choice]['cost']
    print(f'Your change is {change}$, enjoy your {choice}!')


coffee_machine = True
money = 0
while coffee_machine:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if choice == 'off':
        coffee_machine=False
    if choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}$")
    if choice == 'latte' or choice == 'cappuccino' or choice == 'espresso':
        if check_resources(choice):
            print('Please insert coins.')
            quarter = int(input('How many quarters?: '))
            dime = int(input('How many dimes?: '))
            nickle = int(input('How many nickles?: '))
            penny = int(input('How many pennies?: '))
            total = (0.25*quarter)+(.1*dime)+(.05*nickle)+(.01*penny)
            if total >= MENU[choice]['cost']:
                make_coffee()
                money += MENU[choice]['cost']
            else:
                print('Not enough $$$')




