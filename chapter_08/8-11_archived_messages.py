"""Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the 
list of messages. After calling the function, print both of your lists to show that the original list has retained its messages."""

def send_message(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Moving message : {current_message}")
        sent_messages.append(current_message)


messages = ["look who's here", "wow, you smell.", 'did I do that?', 'bye']
sent_messages = []

send_message(messages[:], sent_messages)

print(messages)
print(sent_messages)
