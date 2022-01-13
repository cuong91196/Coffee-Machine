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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    """
    When the user enters “report” to the prompt, shows the current resource values.
    """
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


def check_resources(drink):
    """
    Check if there are enough resources to make that drink.
    :param drink:
    :return True: if enough.
    """
    drink_dict = MENU[drink]["ingredients"]
    for item in drink_dict:
        if resources[item] < drink_dict[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Prompt the user to insert coins.
    :return: Total value of the coins inserted.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    dollars = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return dollars


def check_transaction(money, drink):
    """
    Check that the user has inserted enough money to purchase the drink they selected.
    :param money:
    :param drink:
    :return True: if enough, otherwise False.
    """
    cost = MENU[drink]["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        in_change = money - cost
        resources["money"] += cost
        print("Here is {:.2f} dollars in change.".format(in_change))
        return True


def make_coffee(drink):
    """
    The ingredients to make the drink should be deducted from the coffee machine resources.
    :param drink:
    """
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕. Enjoy!")


def main():
    user_choose = ""
    while user_choose != "off":
        user_choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choose == "report":
            print_report()
        elif user_choose in MENU:
            drink = user_choose
            if check_resources(drink):
                cash = process_coins()
                if check_transaction(cash, drink):
                    make_coffee(drink)


if __name__ == "__main__":
    main()
