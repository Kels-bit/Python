"""  Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments. 
"""

def make_shirt(size, text):
    """This function should print the shirt size and the text that should be printed on the shirt."""
    print(f"\nShirt size: {size.title()}")
    print(f"Text to be printed: {text.title()}")

#Call 1
make_shirt('m', 'python is fun!')

#Call 2
make_shirt(text='python is hard.', size= 'l')


