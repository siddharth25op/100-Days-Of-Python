from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = False

while not is_on:
    items = menu.get_items()
    user_choice = input(f"What would you like? ({items}): ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        is_on = True
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
