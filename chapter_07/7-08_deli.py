#This program excercise is to empty one list into another.

#Create a list for sandwiches.
sandwich_orders = ['ham', 'turkey', 'meatball', 'club', 'tuna']
#Create a empty list
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"{current_sandwich.title()} sandwich is being prepared.")
    finished_sandwiches.append(current_sandwich)

print(f"\nOrders Completed")
print("--------------------")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} Sandwich Status : Complete")
