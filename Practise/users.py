current_users = ['john', 'mark', 'luke', 'matthew', 'paul', 'enoch', 'issiah']
new_users = ['John', 'Jane', 'MARK', 'joseph', 'mary']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user.title()} has already been taken. Please try again!")
    else:
        print(f"{new_user.title()} is available")
print("Thank you!")