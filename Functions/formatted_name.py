def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted
    Args:
        first_name (str): User first name
        last_name (str): Users last name
    Return:
        str: returns a full formatted name
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)

# Without making an agrument optional.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted
    Args:
        first_name (str): User first name
        last_name (str): Users last name
    Return:
        str: returns a full formatted name
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

