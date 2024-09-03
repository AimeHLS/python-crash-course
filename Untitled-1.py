


order = "onions"  # Example value for demonstration purposes
requested_topping = ["pepperoni", "mushrooms", "olives"]

if order in requested_topping:
    print("\nYour topping is on the way.\n")
else:
    available_toppings = ', '.join(requested_topping).title()
    print(f"\nSorry, {order.upper()} is out of stock. Please choose among "
          f"{available_toppings}.")


print()

net_profit =[100,400]

for profit in net_profit:
    if profit <= 100:
         print("\nYou need to think and work harder my friend.\n")
    else:
        print("\nWe have achieved our goal.")
print()

profit = 120
net_profit = []

if profit in net_profit:
    if profit <= 100:
        print("\nYou need to think and work harder my friend.\n")
    else:
        print("\nWe have achieved our goal.")
else:
    print("\nProfit value is not in the net_profit list.")

