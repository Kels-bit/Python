my_foods = ['pizza','falafel', 'carrot cake']

#This doesn't work:
friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy Friend's favorite foods are:")
for food in friends_foods:
    print(food)
