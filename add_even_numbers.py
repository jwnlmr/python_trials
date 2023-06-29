# this adds all even numbers from 1 to 100

def add_even_numbers():
    total = 0
    for even in range(0,101,2):
        # print(even)
        total += even
    print(total)

add_even_numbers()