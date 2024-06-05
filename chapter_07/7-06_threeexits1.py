#In this exercisew you must use a conditional test to exit the loop using programs from existing excersies.
#This is a copy of 7-04_pizzatoppings.py.
#Prompt The user.
prompt = "\nPlease enter the pizza topping you would like on your pizza: "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        add_topping = f"\n{topping.title()} will be added to your pizza."
        print(add_topping)
