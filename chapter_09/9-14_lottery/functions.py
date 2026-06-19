from random import choice
def lottery_machine():
    
    lottery_characters = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E", )

    lottery_picks = 0
    lottery_winners = []
    while lottery_picks < 5:
        numbers = choice(lottery_characters)
        lottery_winners.append(numbers)
        lottery_picks += 1
    print(f"The winning ticket for the lottery:")
    print(lottery_winners)
