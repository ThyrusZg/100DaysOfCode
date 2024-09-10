import time

MENU = {
    "espresso" : {
        "ingredients": {
            "water" : 50,
            "milk":0,
            "coffee" : 18
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24
        },
        "cost" : 3.0,
    }
}
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}

coins = {
    "quarter" : 25,
    "dime" : 10,
    "nickel" : 5,
    "penny" : 1
}

def check_if_enough_resources(drink):
    if drink["water"] <= resources["water"]:
        if drink["milk"] <= resources["milk"]:
            if drink["coffee"] <= resources["coffee"]:
                return True
    return False

def take_user_coins():
    quarters = int(input("Input quarters: "))
    dimes = int(input("Input dimes: "))
    nickels = int(input("Input nickels: "))
    pennies = int(input("Input pennies: "))
    quarters = quarters * coins["quarter"]
    dimes = dimes * coins["dime"]
    nickels = nickels * coins["nickel"]
    pennies = pennies * coins["penny"]
    total_amount = quarters + dimes + nickels + pennies
    return total_amount


def check_if_item_is_paid(amount, item_price):
    if item_price <= amount:
        return True
    else:
        return False

def calculate_return_money(amount, item_price):
    amount_to_return = amount - item_price
    return amount_to_return / 100

def decrement_resources(drink):
    resources["water"] = resources["water"] - drink["water"]
    resources["milk"] = resources["milk"] - drink["milk"]
    resources["coffee"] = resources["coffee"] - drink["coffee"]

def print_resources():
    print(f"Coffe machine has: \n{resources["water"]} ml of water\n{resources["milk"]} ml of milk"
          f"\n{resources["coffee"]} grams of coffee")
    time.sleep(4)

while True:
    print("What would you like to drink? \n 1. espresso\n 2. latte\n 3. cappuccino\n\nFor report type 'report'\nTo "
          "exit type 'exit'")
    user_input = input(": ")
    if user_input == "1" or user_input.lower == "espresso":
        selected_drink = MENU["espresso"]
        if check_if_enough_resources(selected_drink["ingredients"]):
            inserted_coins = take_user_coins()
            if check_if_item_is_paid(inserted_coins,selected_drink["cost"]*100):
                print(f"Your drink espresso is being prepared.")
                time.sleep(3)
                return_money = calculate_return_money(inserted_coins, selected_drink["cost"])
                print(f"Returning {round(return_money,2)} to the user.")
                time.sleep(2)
                decrement_resources(selected_drink["ingredients"])
                print(f"Your espresso is ready!")
                time.sleep(3)
            else:
                print("You did not insert enough money")
                print(f"Returning {round(inserted_coins /100,2)} to the user")
                time.sleep(4)
        else:
            print(f"There is not enough ingredients to prepare espresso!")
            time.sleep(3)
    elif user_input == "2" or user_input.lower == "latte":
        selected_drink = MENU["latte"]
        if check_if_enough_resources(selected_drink["ingredients"]):
            inserted_coins = take_user_coins()
            if check_if_item_is_paid(inserted_coins, selected_drink["cost"]*100):
                print(f"Your drink latte is being prepared.")
                time.sleep(3)
                return_money = calculate_return_money(inserted_coins, selected_drink["cost"])
                print(f"Returning {round(return_money, 2)} to the user.")
                time.sleep(2)
                decrement_resources(selected_drink["ingredients"])
                print(f"Your latte is ready!")
                time.sleep(3)
            else:
                print("You did not insert enough money")
                print(f"Returning {round(inserted_coins / 100, 2)} to the user")
                time.sleep(4)
        else:
            print(f"There is not enough ingredients to prepare latte!")
            time.sleep(3)
    elif user_input == "3" or user_input.lower == "cappuccino":
        selected_drink = MENU["cappuccino"]
        if check_if_enough_resources(selected_drink["ingredients"]):
            inserted_coins = take_user_coins()
            if check_if_item_is_paid(inserted_coins, selected_drink["cost"]*100):
                print(f"Your drink cappuccino is being prepared.")
                time.sleep(3)
                return_money = calculate_return_money(inserted_coins, selected_drink["cost"])
                print(f"Returning {round(return_money, 2)} to the user.")
                time.sleep(2)
                decrement_resources(selected_drink["ingredients"])
                print(f"Your cappuccino is ready!")
                time.sleep(3)
            else:
                print("You did not insert enough money")
                print(f"Returning {round(inserted_coins / 100, 2)} to the user")
                time.sleep(4)
        else:
            print(f"There is not enough ingredients to prepare cappuccino!")
            time.sleep(3)
    elif user_input == "report":
        print_resources()
    elif user_input == "exit":
        print("Thank you for using coffee machine.\n Bye bye :)")
        time.sleep(2)
        for i in range(10):
            print(100*"*")
            time.sleep(0.2)
        break