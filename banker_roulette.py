'''
Write a program that will select a random name from a list of names.
the person selected will pay for everybody's food bill.

You are not allowed to use the choice() function.
'''

import random

def pick_random_name():
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    pick_name = random.randrange(len(names))
    name = names[pick_name]

    print(f'{name.capitalize()} will pay the bill.')
    
pick_random_name()