def send_messages(texts, sent_messages):
    """Print each text message and move it to sent_messages."""
    while texts:
        current_message = texts.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

texts = ['hello there', 'how you doing', 'how is your day going']
sent_messages_list = []

send_messages(texts[:], sent_messages_list)

print("\nOriginal texts list:")
print(texts)

print("\nSent messages:")
print(sent_messages_list)