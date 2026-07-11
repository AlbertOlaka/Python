cities = {
    'porto': {
        'country' : 'portugal',
        'population': 264000,
        'fact': 'porto is the namesake of the entire country',
    },
    'madrid': {
        'country' : 'spain',
        'population': 6800000,
        'fact': 'the city is home to botin, which has been recognized by guinness world records',
    },
    'munich': {
        'country' : 'germany',
        'population': 1600000,
        'fact': 'known for hosting the worlds largest beer festival',
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    country = info['country']
    population = info['population']
    fact = info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population:,}")
    print(f"\tFact: {fact.capitalize()}")
