

print("Enter two numbers to add them:")

first_number = input("\nEnter the first number: ")
second_number = input("\nEnter the second number: ")

    #Exception
try:
    add = int(first_number) + int(second_number)
except ValueError:
    print("One or more of the values you entered is not an integer!")
    print("Check your inputs and try again.")
else:
    print(f"{int(first_number):,} + {int(second_number):,} = {add:,}.")



