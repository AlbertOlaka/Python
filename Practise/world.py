locations = ['spain', 'germany', 'italy', 'lake como', 'france', 'switzerland', 'monaco']
print(locations)

#Using sorted() function to print the list in alphabetical order without modifying the original list.
print(sorted(locations))
print(locations)

#Using sorted() function to print the list in reverse alphabetical order without modifying the original list.
print(sorted(locations, reverse=True))

#Using reverse() method to reverse the order of the list permanently.
locations.reverse()
print(locations)

#Using reverse() method again to reverse the order of the list back to original.
locations.reverse()
print(locations)

#Using sort() method to sort the list permanently in alphabetical order.
locations.sort()
print(locations)

#Using sort() method with reverse=True argument to sort the list permanently in reverse alphabetical order.
locations.sort(reverse=True)
print(locations)