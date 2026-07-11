sandwich_orders = ['pastrami', 'beef sandwich', 'pastrami', 'tuna sandwich', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami!")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"Making your {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

# Display all sandwiches made
print("\nThe below are the sandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())