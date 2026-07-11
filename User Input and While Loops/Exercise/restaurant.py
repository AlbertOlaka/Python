user = input("How many people are in your dinner group today? ")
user = int(user)

if user > 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nYour table is ready.")