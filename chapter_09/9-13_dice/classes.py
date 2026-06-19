from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(f'Rolling Dice with {self.sides} sides.....')
        for roll in range (0,10):
            newroll = randint(1,self.sides)
            print(f"Roll number {roll+1} is {newroll}.")
        print('\n')
            



