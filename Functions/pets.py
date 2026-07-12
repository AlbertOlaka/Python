# Postional Arguments.
def describe_pet(aniaml_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {aniaml_type}")
    print(f"My {aniaml_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword arguments.
def describe_pet(aniaml_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {aniaml_type}")
    print(f"My {aniaml_type}'s name is {pet_name.title()}")

describe_pet(aniaml_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', aniaml_type='dog')

# Default Values.
def describe_pet(pet_name, aniaml_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {aniaml_type}")
    print(f"My {aniaml_type}'s name is {pet_name.title()}")

describe_pet(pet_name='willie')