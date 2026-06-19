print("\nEnter two number to add them.")
print("\nEnter 'q' to exit program.")


while True:
    first_number = input("\nEnter the first number: ")
    if first_number == 'q':
        print("Exit program.")
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        print("Exit Program.")
        break

    try:
       add = int(first_number) + int(second_number)
    except ValueError:
        print("One or more values you entered are not integers!")
        print("Check your inputs and try again.")
    else:
        print(f"{int(first_number):,} + {int(second_number):,} = {add:,}.")
