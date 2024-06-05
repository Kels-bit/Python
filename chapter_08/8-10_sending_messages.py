"""Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""

def send_message(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Moving message : {current_message}")
        sent_messages.append(current_message)


messages = ["look who's here", "wow, you smell.", 'did I do that?', 'bye']
sent_messages = []

send_message(messages, sent_messages)

print(messages)
print(sent_messages)
