def love_calculator():
    print("Welcome to the love calculator.\nI will determine your compatibility with your partner.")
    name1 = input("What is your name?\n")
    name2 = input("What is their name?\n")
    names = name1 + name2
    true_total = 0
    love_total = 0
    for x in names:
        if x.upper() == 'T' or x.upper() == 'R' or x.upper() == 'U' or x.upper() == 'E':
            true_total += 1
    for y in names:
        if y.upper() == 'L' or y.upper() == 'O' or y.upper() == 'V' or y.upper() == 'E':
            love_total += 1
    final_score = str(true_total) + str(love_total)

    if int(final_score) <= 10 or int(final_score) >= 90:
        print(f'Your score is {final_score}, you go together like coke and mentos.')
    elif int(final_score) >= 40 and int(final_score) <= 50:
        print(f'Your score is {final_score}, you are alright together.')
    else:
        print(f'Your score is {final_score}')
love_calculator()
