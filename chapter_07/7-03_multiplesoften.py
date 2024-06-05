#Prompt the user.
number = input("Enter a number, and I'll tell you if it's a multiple of ten: ")
number = int(number)

#Output
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")
