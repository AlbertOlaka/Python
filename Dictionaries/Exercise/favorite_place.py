favorite_places = {
    'lydia': ['greece', 'france', 'italy'],
    'albert': ['portugal', 'spain'],
    'joseph': ['brazil', 'kenya', 'germany']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places:")
    for place in places:
        print(f"\t- {place.title()}")