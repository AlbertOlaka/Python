# Testing multiple Conditions.
# Use to check multiple conditions using if statements without the elif or else blocks.
# This technique makes sense when more than one condition could be true and you want to act onevery condition that is true.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")