from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        coffee_maker.report()
        money_maker.report()
    if choice == "refill":
        coffee_maker.refill()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_maker.make_payment(drink.cost):
            coffee_maker.make_coffee(order=drink)








