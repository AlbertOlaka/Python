rivers = {
    'nile' : 'egypt',
    'amazon' : 'peru',
    'yangtze': 'china'
}

for r, n in rivers.items():
    print(f"The {r.title()} runs through {n.title()}")

for r in rivers.keys():
    print(f"\n{r.title()}")

for n in rivers.values():
    print(f"\n{n.title()}")

# Exercise 6.6
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

friends = ['phil', 'sarah', 'mark', 'luke']
for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name].title()
        print(f"Hi {name.title()}, thank you for taking the poll.")
    else:
        print(f"Hi {name.title()}, kindly take our poll.")