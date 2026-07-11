prompt = "\nPlease enter the pizza toppings you would like: "
prompt += "\n(Enter 'quit' when done.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f" Adding {message.title()} to your pizza.")