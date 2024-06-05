num_list = []

for num in range (1, 10):
 num_list.append(num)

for num in num_list:
    if num == 1:
        print("1st")
    elif num == 2:
        print('2nd')
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")

