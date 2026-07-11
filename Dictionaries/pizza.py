# A LIST IN A DICTIONARY
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " 
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#Example 2:
favorite_languages = {
    'jen': ['python', 'rest'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskel'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")