#Treasure Island Game

import time

def treasure_island():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nGood luck!\n")
    left_or_right = input("Which path would you like to take? L for left R for right\n")
    if left_or_right.upper() == 'L':
        print('''\nYou come out the other side and see a river blocking your path.\nThere are ill tempered trout swimming in the water.\nWhat will you do?''')
        river = input("\nSwim quickly across or wait for an opening? Swim or Wait\n")
        if river.lower() == "wait":
            print('''
            While you are waiting a rabbit hops over to you.
            You toss the rabbit into the water to distract the trout and quickly swim across.
            Some may consider you to be a monster.

            Not me, though.

            I hate rabbits....
            ''')
            time.sleep (3)
            print('''
            Anyway...

            On the other side you come to a weird looking structure. 
            You can see a boat but the only way to it is through the structure.
            ''')
            time.sleep (1)
            door = input("\nInside the structure are three differently colored doors.\nOnly one will lead to the boat and treasure. The others....?\nDeath\nRed, Yellow, or Blue?\n")
            if door.lower() == 'yellow':
                print('''
                You see the treaure!, you grab it and head for the boat immediately.
                The boat is mysteriously in great condition with navigation equipment in tact.
                You decide to take it home.
                As you sail away you see someone frantically running from the structure, shouting inaudibly, and flailing their arms.
                You ignore them, turn to the horizon, and give a big sigh of relief.....
                ''')
                time.sleep(5)
                print('''
                and when you get home you give the coordinates to the coast guard so they can rescue the guy still on the island.

                See? you're not all bad. :)
                ''')
            elif door.lower() == 'red':
                print('''
                You walk into a dark room with an odd smell and can't see very well.
                you remember you brought a pack of matches you picked up from the hotel before coming here.
                As you light a match you can see drums of boat fuel. Some have leaked onto the floor.
                You scan the room continuously looking for something to help you.
                You forgot about the match you were holding and you drop it after burning your finger tips.
                The whole room goes up in flames and you die a fiery death.
                The end.
                ''')
            elif door.lower() == 'blue':
                print('''
                You are immediately eaten by wild beasts. Game over.
                ''')
            else:
                print('''
                You do nothing and die of dysentary.
                ''')
        else:
            print('''
            You think nothing of it and just go.
            You don't make it five feet before your flesh is all but gone.
            Game over, man!
            ''')
    else:
        print('''
        You stumble into a hole leading to beautiful caverns below.
        Pretty neat, but you are impaled on a stalagmite when you land, and you die.
        Game over.
        ''')
    time.sleep(1)
    play_again = input("\nWould you like to try again? Y or N\n")
    if play_again.lower() == 'y':
        return treasure_island()
    else:
        exit()
treasure_island()