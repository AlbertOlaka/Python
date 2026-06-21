# Using the sort() method to sort a list permanetly.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Using the reverse=true argument to sort the list in reverse order.
cars.sort(reverse=True)
print(cars)

# Using the sorted() function to sort a list temporarily.
print("Here is the original list: ")
print(cars)

print("\nHere is the new list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

# Printing a list in reverse order using reverse() method.
cars.reverse()
print(cars)

# Finding the length of a list using len() function.
print(len(cars))