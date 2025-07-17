from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine=MoneyMachine()
coffeemaker=CoffeeMaker()
menu=Menu()


loop=True
while loop:
   op=menu.get_items()
   choice=input(f"what would you like({op}):").lower()
   if choice=='off':
      loop=False
   elif choice=='report':
      coffeemaker.report()
      moneymachine.report()
   else:
      drink=menu.find_drink(choice)
      if coffeemaker.is_resource_sufficient(drink):
         if moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)


      