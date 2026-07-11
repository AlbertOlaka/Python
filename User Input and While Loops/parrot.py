# Example 1
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Example 2
names = []

message = input("Enter your name: ")
names.append(message)

for name in names:
    print(f"Hello, {name.title()}!")