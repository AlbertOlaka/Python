def make_sandwich(size, *ingredients):
    print(f"\n Making a {size} sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('medium', 'pepperoni')
make_sandwich('large', 'pepperoni', 'onion', 'chicken', 'chillies', 'tomato')