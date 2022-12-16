import random

randomNumber = random.randint(0,9)

for x in range(5):
    guessNumber = int(input("Guess number from 0 to 9 : "))
    if guessNumber == randomNumber:
        print("Congrats!!! u did it")
        break
    else:
        print("u {} try".format(x))
