print("--------------------")
print("Play TicTacToe!!!!")
print("--------------------")
print()
print("Positions:- ")
print()
print("  1  |  2  |  3  ")
print("-----+-----+-----")
print("  4  |  5  |  6  ")
print("-----+-----+-----")
print("  7  |  8  |  9  ")
print()


tic=[" ", " ", " ", " ", " ", " ", " ", " ", " "]

def result():
        print(f"  {tic[0]}  |  {tic[1]}  |  {tic[2]}  ")
        print("-----+-----+-----")
        print(f"  {tic[3]}  |  {tic[4]}  |  {tic[5]}  ")
        print("-----+-----+-----")
        print(f"  {tic[6]}  |  {tic[7]}  |  {tic[8]}  ")
while True:
    print()
    if not " " in tic:
        print("Tie")
        break
    inp=str(input("X or O: ")).lower()
    if inp=="x":
        place=int(input("Choose a Position number: "))
        if place==1:
            tic.pop(0)
            tic.insert(0,"X")
            result()
        elif place==2:
                    tic.pop(1)
                    tic.insert(1,"X")
                    result()
        elif place==3:
                tic.pop(2)
                tic.insert(2,"X")
                result()
        elif place==4:
                    tic.pop(3)
                    tic.insert(3,"X")
                    result()
        elif place==5:
                    tic.pop(4)
                    tic.insert(4,"X")
                    result()
        elif place==6:
                    tic.pop(5)
                    tic.insert(5,"X")
                    result()
        elif place==7:
                    tic.pop(6)
                    tic.insert(6,"X")
                    result()
        elif place==8:
                    tic.pop(7)
                    tic.insert(7,"X")
                    result()
        elif place==9:
                    tic.pop(8)
                    tic.insert(8,"X")
                    result()
        else:
                print("Not valide position")
    elif inp=="o":
            place=int(input("Choose a Position number: "))
            if place==1:
                tic.pop(0)
                tic.insert(0,"O")
                result()
            elif place==2:
                        tic.pop(1)
                        tic.insert(1,"O")
                        result()
            elif place==3:
                    tic.pop(2)
                    tic.insert(2,"O")
                    result()
            elif place==4:
                        tic.pop(3)
                        tic.insert(3,"O")
                        result()
            elif place==5:
                        tic.pop(4)
                        tic.insert(4,"O")
                        result()
            elif place==6:
                        tic.pop(5)
                        tic.insert(5,"O")
                        result()
            elif place==7:
                        tic.pop(6)
                        tic.insert(6,"O")
                        result()
            elif place==8:
                        tic.pop(7)
                        tic.insert(7,"O")
                        result()
            elif place==9:
                        tic.pop(8)
                        tic.insert(8,"O")
                        result()
            else:
                    print("Not a valide position")
    else:
            print(f"{inp} Not a Valid Move")
    print("---------------------------------------------------------")
    if tic[0]==tic[1]==tic[2]=="X":
            print("X won")
            break
    elif tic[0]==tic[1]==tic[2]=="O":
            print("O won")
            break
    else:
        pass
    if tic[3]==tic[4]==tic[5]=="X":
            print("X won")
            break
    elif tic[3]==tic[4]==tic[5]=="O":
            print("O won")
            break
    else:
        pass
    if tic[6]==tic[7]==tic[8]=="X":
            print("X won")
            break
    elif tic[6]==tic[7]==tic[8]=="O":
            print("O won")
            break
    else:
        pass
    if tic[0]==tic[3]==tic[6]=="X":
            print("X won")
            break
    elif tic[0]==tic[3]==tic[6]=="O":
            print("O won")
            break
    else:
        pass
    if tic[1]==tic[4]==tic[7]=="X":
            print("X won")
            break
    elif tic[1]==tic[4]==tic[7]=="O":
            print("O won")
            break
    else:
        pass
    if tic[2]==tic[5]==tic[8]=="X":
            print("X won")
            break
    elif tic[2]==tic[5]==tic[8]=="O":
            print("O won")
            break
    else:
        pass
    if tic[0]==tic[4]==tic[8]=="X":
            print("X won")
            break
    elif tic[0]==tic[4]==tic[8]=="O":
            print("O won")
            break
    else:
        pass
    if tic[2]==tic[4]==tic[6]=="X":
            print("X won")
            break
    elif tic[2]==tic[4]==tic[6]=="O":
            print("O won")
            break
    else:
        pass
    print()

print("Game Over")
