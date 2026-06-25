favourite_pizaa = ['chicken tikka', 'peri peri chicken', 'bbq beef']
for pizza in favourite_pizaa:
    print(pizza)
    print(f"I love the {pizza.title()} pizza")

print("I really like having pizza, especially on the days when their are offers on Tuesday when it but one get one free. I really love pizza.")

# Making a copy of a list
favourite_pizaa = ['chicken tikka', 'peri peri chicken', 'bbq beef']
friends_pizzas = favourite_pizaa[:]

favourite_pizaa.append('bbq chicken')
friends_pizzas.append('hawaian')

print("\nMy favourite pizzas are:")
for pizza in favourite_pizaa:
    print(pizza)

print("\nMy friend'f favourite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)