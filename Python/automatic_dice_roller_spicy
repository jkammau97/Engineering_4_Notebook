# Automatic Dice Roller Spicy (with error detection)

# Written by [Bob Kammauff]

import random
from random import randint

print("Automatic Dice Roller Spicy")
print("Press Enter to roll")

while True:
    print("How many sides?")
    sidesRaw = input()
    print("How many rolls?")
    rollsRaw = input()
    try:
        sidesInt = int(sidesRaw)
        rollsInt = int(rollsRaw)
        sidesInt = sidesInt/sidesInt/rollsInt*rollsInt*sidesInt #just an identity, but if it equals zero it'll throw an error that I can catch
    except ValueError:
        raise print("you put in some funky values that jacked up my vibe; try again")
        continue #restarts loop back to beginning
    except ZeroDivisionError:
        print("haha look at the funny guy trying to roll a die with zero sides. TRY AGAIN!")
        continue
    while True:
        print("You rolled:")
        for i in range(rollsInt):
            print(str(random.randint(1,sideInt)))
        print("hit enter to roll again with the same settings, c then enter to update the options, or x then enter to exit")
        user = input()
        if user != '':
            break #if its not a roll again command, back out to the main while loop so that you can kill the main while loop
        print("roll again!")
    if user == 'x':
        print("Goodbye!")
        break
