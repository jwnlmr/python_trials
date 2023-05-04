#Rock paper scissors game
import random
def rps_game():
    print('''
 ___                                                                  _
/__/|__                                                            __//|
|__|/_/|__                                                       _/_|_||
|_|___|/_/|__                                                 __/_|___||
|___|____|/_/|__                                           __/_|____|_||
|_|___|_____|/_/|_________________________________________/_|_____|___||
|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||
|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||
|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/
    ''')
    print('\nWelcome to Rock, Paper, Scissors\n')
    rock = '''
    _______
---'   ____)
       (_____)
       (_____)
       (____)
---.__(___)
    
'''
    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    '''
    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''


    player_input = input("Please pick: Rock = 0, Paper = 1, Scissors = 2: ")
    cpu_input = random.randrange(2)
    if int(player_input) == 0:
        if int(cpu_input) == 0:
            print(f"{rock}\n Computer chose:\n {rock}\nTie game.")
        elif int(cpu_input) == 1:
            print(f"{rock}\n Computer chose:\n {paper}\nComputer wins!")
        elif int(cpu_input) == 2:
            print(f"{rock}\n Computer chose:\n {scissors}\nYou win!")
    elif int(player_input) == 1:
        if int(cpu_input) == 0:
            print(f"{paper}\n Computer chose:\n {rock}\nYou win!")
        elif int(cpu_input) == 1:
            print(f"{paper}\n Computer chose:\n {paper}\nTie game.")
        elif int(cpu_input) == 2:
            print(f"{paper}\n Computer chose:\n {scissors}\nComputer Wins!")
    elif int(player_input) == 2:
        if int(cpu_input) == 0:
            print(f"{scissors}\n Computer chose:\n {rock}\nComputer wins!")
        elif int(cpu_input) == 1:
            print(f"{scissors}\n Computer chose:\n {paper}\nPlayer wins!")
        elif int(cpu_input) == 2:
            print(f"{scissors}\nComputer chose:\n {scissors}\nTie Game")
    else:
        print("Invalid response")
        exit()
    play_again = input("\nWould you like to play again? y for yes, n for no: ")
    if play_again.lower() == 'y':
        return rps_game()
    else:
        exit()
rps_game()