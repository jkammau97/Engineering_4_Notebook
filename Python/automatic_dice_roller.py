# Automatic Dice Roller

# Written by [Bob Kammauff]

import random
from random import randint

print("Automatic Dice Roller")
print("Press Enter to roll")
print("x then enter to quit")
while True:
    user = input()
    if user == 'x':
        print("Goodbye!")
        break
    if user == '':
        roll = str(random.randint(1,6)) # random number from 1 to 6
        print("You rolled: " + roll)
