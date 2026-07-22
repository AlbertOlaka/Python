from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)

# Working with a File's Contents
# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_strings = ''
# for line in lines:
#     pi_strings += line.lstrip()

# print(pi_strings)
# print(len(pi_strings))