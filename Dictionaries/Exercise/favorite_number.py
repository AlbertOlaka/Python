favourite_number = {
    'jane' : [10, 45],
    'joseph' : [44, 90],
    'albert' : [40],
    'davis' : [35, 50],
    'max' : [1],
}

for name, numbers in favourite_number.items():
    label = "numbers are" if len(numbers) > 1 else "number is"
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")