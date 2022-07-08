Menu = {
    'espresso': {
        'Water': 50,
        'Coffee': 18,
        'Milk': 0,
        'Price': 1.50
    },
    'latte': {
        'Water': 200,
        'Coffee': 24,
        'Milk': 150,
        'Price': 2.50
    },
    'cappuccino': {
        'Water': 250,
        'Coffee': 24,
        'Milk': 100,
        'Price': 3.00
    }
}
total = {
    'Water': 300,
    'Coffee': 100,
    'Milk': 200,
    'Price': 0
}
flag = True
profit = 0


def check_resources(choice, total):
    if total['Water'] < choice['Water']:
        print("Sorry there is not enough water.")
        return False
    elif total['Coffee'] < choice['Coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif total['Milk'] < choice['Milk']:
        print("Sorry there is not enough milk.")
        return False


def check_coins(cost, choice, profit):
    if cost < choice['Price']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cost == choice['Price']:
        profit += cost
        return profit
    elif cost > choice['Price']:
        change = round(cost - choice['Price'], 2)
        profit += cost
        print(f"Here is {change} dollars in change.")
        return profit


while flag is True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    choices = choice
    if choice == 'off':
        flag = False
    elif choice == 'report':
        print(f"Water: {total['Water']}ml")
        print(f"Coffee: {total['Coffee']}g")
        print(f"Milk: {total['Milk']}ml")
        print(f"Price: ${total['Price']}")
    else:
        if choice == 'espresso':
            choice = Menu['espresso']
        elif choice == 'latte':
            choice = Menu['latte']
        elif choice == 'cappuccino':
            choice = Menu['cappuccino']
        check = check_resources(choice, total)
        if check is not False:
            quarter = int(input("Process coins.\nHow many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            cost = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
            profit = check_coins(cost, choice, profit)
            if profit is not False:
                total['Water'] -= choice['Water']
                total['Milk'] -= choice['Milk']
                total['Coffee'] -= choice['Coffee']
                total['Price'] += choice['Price']
                print(f"Here is your {choices}. Enjoy!!")
