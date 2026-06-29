# Simple if statements
alien_color = 'green', 'yellow', 'red'
if 'green' in alien_color:
    print("You have just earned 5 points!")
if 'pink' in alien_color:
    print("You have just earned 5 points!")

# If-Else chain
alien_color = 'red'
if 'green' in alien_color:
    print("\nYou have just earned 5 points!")
else:
    print("\nYou have just earned 10 points!")

# If-Elif-Else chain
alien_color = 'red'
if 'green' in alien_color:
    print("\nYou have just earned 5 points!")
elif 'yellow' in alien_color:
    print("You have just earned 10 points!")
else:
    print("\nYou have just earned 15 points!")