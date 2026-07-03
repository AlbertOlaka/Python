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
    'python' : 'A high level language used for backend development and AI engineering.',
    'c' : 'A low level language used for systems programming and hardware interaction.',
    'html' : 'A markup language used for structuring content on the web.',
    'javascript' : 'A frontend language used to make web pages interactive.',
    'c#' : 'A low level language developed by Microsoft for application development.',
}

print(f"Python:\n\t{glossary['python']}")
print(f"C:\n\t{glossary['c']}")
print(f"HTML:\n\t{glossary['html']}")
print(f"Javascript:\n\t{glossary['javascript']}")
print(f"C#:\n\t{glossary['c#']}")