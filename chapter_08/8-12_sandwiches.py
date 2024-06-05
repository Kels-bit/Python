""" Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time. """

def sandwich_order(*toppings):
    print("\nMaking Sandwich:")
    for topping in toppings:
        print(f"- {topping}")

sandwich_order('11', 'pickles', 'ham', 'cheese')
sandwich_order('bacon', 'turkey')
sandwich_order('tomato', 'onion','no bread', 'mayo')


