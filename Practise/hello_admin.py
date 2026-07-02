usernames = ['john', 'mark', 'luke', 'matthew', 'paul', 'admin', 'enoch', 'issiah']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again")
print("Thank you")

# No users
if usernames:
    for username in usernames:
        print(f"Hello {username.title()}")
else:
    print("We need to find some users!")