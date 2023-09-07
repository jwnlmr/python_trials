# this code emulates the fizzbuzz game.
'''
The code will iterate through a range of numbers from 1 to n.
if a number is divisible by 3 it will print 'fizz'
if a number is divisible by 5 it will print 'buzz'
if a number is divisible by 3 and 5 it will print 'fizzbuzz'
if the number is not divisible by either it will print the number
'''

def fizz_buzz() -> str: 
    for n in range(1, 101):
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)
fizz_buzz()