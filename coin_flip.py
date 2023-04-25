# Basic virtual coin flip program
import random

def flip_coin():
    flip = random.randrange(2)

    if flip == 1:
        side = 'heads'
    elif flip == 0:
        side = 'tails'
    else:
        print("It landed on its side")
    print(f'It landed on {side}')

flip_coin()