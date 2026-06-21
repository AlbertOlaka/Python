# Removing the last item in a list using the pop() method
motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Removing an item from any position in a list using the pop() method and printing it with f strings
motorcycles = ['honda', 'suzuki', 'yamaha']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# Poping Items from Any position in a list
motorcycles = ['honda', 'suzuki', 'yamaha']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a 2024 {first_owned.title()}")