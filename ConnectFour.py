import Games.Design as Design

row1 = ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]
row2 = ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]
row3 = ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]
row4 = ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]
row5 = ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]
row6 = ["⚪","⚪","⚪","⚪","⚪","⚪","⚪"]

def board():
    print()
    print(" ".join(row1))
    print(" ".join(row2))
    print(" ".join(row3))
    print(" ".join(row4))
    print(" ".join(row5))
    print(" ".join(row6))
    print(" 1  2  3  4  5  6  7")

row = [row6,row5,row4,row3,row2,row1]
num = 0
while True:
    while True:
        board()
        if "⚪" not in row6 and "⚪" not in row5 and "⚪" not in row4 and "⚪" not in row3 and "⚪" not in row2 and "⚪" not in row1:
            print(Design.shape1("It's a draw"))
            exit() 
        
        try:
            choice_player1 = int(input("\nPlayer1: choose a column: "))
        except ValueError:
            print(Design.shape1("You must enter a number between 1 to 7"))
            continue
        if choice_player1 in (1,2,3,4,5,6,7):
    
            for X in row:
                if X[ choice_player1 - 1 ] == "⚪":
                    X[ choice_player1 - 1 ] = "🔴"
                    break
            else:
                print(Design.shape1("You can not choose this column because it's full"))
                continue
        else:
            print(Design.shape1("You must enter a number between 1 to 7"))
            # print(Design + " --< You must enter a number between 1 to 7 >--")
            continue
        break
    
    for X in row:
        number = 0
        while number <= 3:
            if X[number] == "🔴" and X[number+1] == "🔴" and X[number+2] == "🔴" and X[number+3] == "🔴":
                board()
                print(Design.shape1("Player one won"))
                exit()
            elif number == 3:
                break
            number += 1
    for number in (0,1,2,3,4,5,6):
        row_num = 0
        while row_num <= 2:
            if (row[row_num])[number] == "🔴" and (row[row_num+1])[number] == "🔴" and (row[row_num+2])[number] == "🔴" and (row[row_num+3])[number] == "🔴":
                board()
                print(Design.shape1("Player one won"))
                exit()
            elif row_num == 2:
                break
            row_num += 1
    for number in (0,1,2,3):
        row_num = 0
        while row_num <= 2:
            if (row[row_num])[number] == "🔴" and (row[row_num+1])[number+1] == "🔴" and (row[row_num+2])[number+2] == "🔴" and (row[row_num+3])[number+3] == "🔴":
                board()
                print(Design.shape1("Player one won"))
                exit()
            elif row_num == 2:
                break
            row_num += 1
    for number in (0,1,2,3):
        row_num = 0
        while row_num <= 2:
            if (row[row_num+3])[number] == "🔴" and (row[row_num+2])[number+1] == "🔴" and (row[row_num+1])[number+2] == "🔴" and (row[row_num])[number+3] == "🔴":
                board()
                print(Design.shape1("Player one won"))
                exit()
            elif row_num == 2:
                break
            row_num += 1
    num = 0

    while True:
        board()
        if "⚪" not in row6 and "⚪" not in row5 and "⚪" not in row4 and "⚪" not in row3 and "⚪" not in row2 and "⚪" not in row1:
            print(Design.shape1("It's a draw"))
            exit() 
        
        try:
            choice_player2 = int(input("Player2: choose a column: "))
        except ValueError:
            print(Design.shape1("You must enter a number between 1 to 7"))
            continue
        if choice_player2 in (1,2,3,4,5,6,7):
    
            for X in row:
                if X[ choice_player2 - 1 ] == "⚪":
                    X[ choice_player2 - 1 ] = "🔵"
                    break
            else:
                print(Design.shape1("You can not choose this column because it's full"))
                continue
        else:
            print(Design.shape1("You must enter a number between 1 to 7"))
            continue
        break

    for X in row:
        number = 0
        while number <= 3:
            if X[number] == "🔵" and X[number+1] == "🔵" and X[number+2] == "🔵" and X[number+3] == "🔵":
                board()
                print(Design.shape1("Player two won"))
                exit()
            elif number == 3:
                break
            number += 1
    for number in (0,1,2,3,4,5,6):
        row_num = 0
        while row_num <= 2:
            if (row[row_num])[number] == "🔵" and (row[row_num+1])[number] == "🔵" and (row[row_num+2])[number] == "🔵" and (row[row_num+3])[number] == "🔵":
                board()
                print(Design.shape1("Player two won"))
                exit()
            elif row_num == 2:
                break
            row_num += 1
    for number in (0,1,2,3):
        row_num = 0
        while row_num <= 2:
            if (row[row_num])[number] == "🔵" and (row[row_num+1])[number+1] == "🔵" and (row[row_num+2])[number+2] == "🔵" and (row[row_num+3])[number+3] == "🔵":
                board()
                print(Design.shape1("Player two won"))
                exit()
            elif row_num == 2:
                break
            row_num += 1
    for number in (0,1,2,3):
        row_num = 0
        while row_num <= 2:
            if (row[row_num+3])[number] == "🔵" and (row[row_num+2])[number+1] == "🔵" and (row[row_num+1])[number+2] == "🔵" and (row[row_num])[number+3] == "🔵":
                board()
                print(Design.shape1("Player two won"))
                exit()
            elif row_num == 2:
                break
            row_num += 1
    num = 0