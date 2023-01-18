MENU = {
    "espresso": {
        "ingredients":  {
            "water": 150,
            "milk": 50,
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

should_continue = True
while should_continue:
    user_choice = input("What would you like? (espresso/latte/cappuccino)\n")


    def prompt():

        quarters = int(input("how many quarters?:"))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?:"))
        pennies = int(input("how many pennies?:"))

        
        process_coin = quarters * 0.25, dimes * 0.1, nickles * 0.05, pennies * 0.01
        final_process = print(round(sum(process_coin,2)))
        final_process_ = print(str("$" + final_process))

        
    if user_choice == "espresso":
        prompt()

    elif user_choice == "latte":
        prompt()
    elif user_choice == "cappuccino":
        prompt()
    if user_choice == "off":
        should_continue = False

    else:
        if user_choice == "report":
            resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }