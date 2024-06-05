""" Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message. 
"""

def make_shirt(size = 'l', text = 'i love python.'):
    """This function should print the shirt size and the text that should be printed on the shirt."""
    print(f"\nShirt size: {size.title()}")
    print(f"Text to be printed: {text.title()}")

#Call 1
make_shirt('m')

#Call 2
make_shirt(text='python is hard.')


