cities = ['valencia', 'madrid', 'barcelona', 'sevilla', 'zaragoza', 'porto', 'lake como']
print(cities)

#Using sorted() function to print the list in alphabetical order without modifying the original list.
print(sorted(cities))
print(cities)

#Using sorted() function to print the list in reverse alphabetical order without modifying the original list.
print(sorted(cities, reverse=True))

#Using reverse() method to reverse the order of the list permanently.
cities.reverse()
print(cities)

#Using reverse() method again to reverse the order of the list back to original.
cities.reverse()
print(cities)

#Using sort() method to sort the list permanently in alphabetical order.
cities.sort()
print(cities)

#Using sort() method with reverse=True argument to sort the list permanently in reverse alphabetical order.
cities.sort(reverse=True)
print(cities)