cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

# More concise way to do it.
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# List comprehension
cubes = [value ** 3 for value in range(1,11)]
print(cubes)