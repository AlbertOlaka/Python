# Removing an item by value
motorcycles = ['honda', 'suzuki', 'yamaha', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Removing a value from a list and print a reason.
motorcycles = ['honda', 'suzuki', 'yamaha', 'ducati']
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")