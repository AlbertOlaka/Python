# Using the range() function.
for value in range(1, 5):
    print(value)

# Using range() to make a list of numbers.
numbers = list(range(1, 6))
print(numbers)

# Using range to generate a list of even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Example: Consider how to make a list of the first 10 square numbers(that is, the square of each integer
# from 1 through 10). In python 2 asterisks represents exponents.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# More concise way to do it.
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)