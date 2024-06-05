"""Make a list containing a series of short text messages. Pass the list to a function called show_messages(), 
which prints each text message.
"""

def short_message(messages):
    for msg in messages:
        print(msg)


messages = ["look who's here", "wow, you smell.", 'did I do that?', 'bye']
short_message(messages
              )

