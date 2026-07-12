# Exercise 8-3
def make_shirt(shirt_size, shirt_info):
    """Display the size and info about shirt
    Args:
        shirt_size (str): Tells us the T-shirt size
        shirt_info (str): Tells us what to be printed on the shirt 
    Returns:
        None
    """
    print(f"This is a {shirt_size} shirt and with the message: {shirt_info}")

make_shirt('medium', 'manchester united')
make_shirt(shirt_size='large', shirt_info='manchester united')

# Exercise 8-4
def make_shirt(shirt_size='large', shirt_info='I love Python'):
    """Display the size and info about shirt
    Args:
        shirt_size (str): Tells us the T-shirt size
        shirt_info (str): Tells us what to be printed on the shirt 
    Returns:
        None
    """
    print(f"\nThis is a {shirt_size} shirt and with the message: {shirt_info}")

make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_size='small', shirt_info='I love Functions')

# Exercise 8-5
def describe_city(city_name, city_country='spain'):
    """Display the name of a city and what country it's in
    Args:
        city_name (str): Tells us the name is the city.
        city_country (str): Tells us the country the city is in.
    Returns:
        None
    """
    print(f"\n{city_name.title()} is in {city_country.title()}")

describe_city('barcelona')
describe_city(city_name='madrid')
describe_city('porto', 'portugal')

