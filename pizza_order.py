def order_pizza():
    print("Welcom to Python Pizza Deliveries")
    size = input("what size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    final = 0
    if size.upper() == 'S':
        final += 15
    elif size.upper() == 'M':
        final += 20
    elif size.upper() == 'L':
        final += 25
    
    if add_pepperoni.upper() == 'Y':
        final += 2
    if extra_cheese.upper() == 'Y':
        final += 1
    
    print(f'Your final bill is: ${final}')
order_pizza()