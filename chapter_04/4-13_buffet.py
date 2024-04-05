dishes = ('steak', 'chicken', 'lobster', 'duck', 'lamb')

print("This restaurant offers dishes from list below:")
for dish in dishes:
    print(dish.title())

#Failure to overwrite tuple
dishes[3] = elk #This line should be comment out for the program to work.

#Rewrite the tuple.
dishes = ('steak', 'pork', 'lobster', 'elk', 'lamb')
print("The updated menu for tonight is:")
for dish in dishes:
    print(dish.title())
