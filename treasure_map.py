# 🚨 Don't change the code below 👇
def mark_map():
    row1 = ["⬜️","️⬜️","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    
    x_pos = int(position[0]) - 1
    y_pos = int(position[1]) - 1
    map[y_pos][x_pos] = ' X'

    print(f"{row1}\n{row2}\n{row3}")

mark_map()