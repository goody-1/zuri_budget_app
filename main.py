import budget

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

print(f"This is the food balance: \u20A6{food.get_balance()}")

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

print(f"This is the food balance after transfer: \u20A6{food.get_balance()}")

print(f"The clothing balance is \u20A6{clothing.get_balance()}")

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

