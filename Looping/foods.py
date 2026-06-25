my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#To prove we have two separate list:
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)

#The below doesn't work and will have the same list items
# friend_foods = my_foods