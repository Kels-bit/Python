my_pizzas = ['pepperoni', 'cheese', 'sasuage', 'veggie']

#Make a copy of the list.
friend_pizza = my_pizzas[:]

#Add a pizza to the orignal list.
my_pizzas.append('pineapple')
#Add a pizza to the new list.
friend_pizza.append('buffalo')
#Output
print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
      print(pizza)
