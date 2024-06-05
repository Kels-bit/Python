#Create an actual dictionary (glossary) using a dictionary(whew) using programming words from previous chapters (with a loop).
glossary = {
        'variables':'are containers for storing data',
        'strings':'are a series of characters',
        'lists':'are a collection of items in a particualr order',
        'if statments' :'are a control structure that controls the flow of the program',
        'loops':'allows you perform the same action repeatedly',
        'floats':'any number with a decmal point',
        'constant':'a variable whose value stays the same throughout the life of a program',
        'sorted() function':'lets you display your list in a particular order',
        'comments': 'allows you to write notes in your program',
        'slice': 'allows you to work with a specific group of items in a list'
         }

for word, defin in glossary.items():
    print(f"\n{word.title()}:")
    print(f"\t{defin}.")




