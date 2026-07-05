person = {
    'first_name' : 'john',
    'last_name' : 'mayor',
    'age' : 25,
    'city' : 'nairobi'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Exercise 6.2
favourite_number = {
    'jane' : 10,
    'joseph' : 44,
    'albert' : 40,
    'davis' : 35,
    'max' : 1,
}

print(f"Jane's favourite number is {favourite_number['jane']}")
print(f"Joseph's favourite number is {favourite_number['joseph']}")
print(f"Alberts's favourite number is {favourite_number['albert']}")
print(f"Davis's favourite number is {favourite_number['davis']}")
print(f"Max's favourite number is {favourite_number['max']}")

# Exercise 6.3
glossary = {
    'variables' : 'A label that you can assign a value.',
    'comments' : 'Used to write something the programmer does not want to run.',
    'method' : 'An action Python can perform on a piece of data.',
    'string' : 'A series of characters.',
    'whitespace' : 'Refers to any non-printing characters such as, spaces, tabs or end of line symbols.',
    'syntax' : 'Occurs when python does not recognize a section of your program as valid python code.',
    'constants' : 'This is a variable whose value stays the same throughout the life of a program.',
    'arbitary numbers' : 'Is a value or variable chosen without a specific rule,pattern or underlyig formular.',
    'list' : 'It is a collection of items in a particular order.',
    'reverse method' : 'The methos reverses the original order of a list.'
}

for key, value in glossary.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value}")