#This program excercise is to empty one list into another.

#Create a list for sandwiches.
sandwich_orders = ['pastrami', 'ham', 'turkey', 'pastrami', 'meatball', 'club', 'tuna', 'pastrami']
#Create a empty list
finished_sandwiches = []
print(f"ANNOUNCEMENT: THE DELI IS OUT OF PASTRAMI!!!!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"{current_sandwich.title()} sandwich is being prepared.")
    finished_sandwiches.append(current_sandwich)

print(f"\nOrders Completed")
print("--------------------")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} Sandwich Status : Complete")
