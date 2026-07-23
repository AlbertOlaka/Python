from pathlib import Path

names = []

while True:
    guest = input("What is your name? (Enter 'quit' when you are finished.)")

    if guest == 'quit':
        break
    else:
        names.append(guest)
        print(f"{guest} added to the list.")

path = Path('guest_book.txt')
contents = "\n".join(names)
path.write_text(contents)