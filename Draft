import random


def mapChooser():
    print("Welcome to the Wild West Shootout!")
    
    print("\nTraining Room (Tutorial)")
    print("Plano, Texas (Easy)")
    print("Tuscon, Arizona (Medium)")
    print("Las Vegas, Nevada (Hard)")


def tutorial():
    print("Welcome to the Training Range!\n")
    print("You (Player 1) and the Computer will be hiding behind barrels.")
    print("Since this is the tutorial, both players will start with three barrels but as the difficulty increases the computer will gain more barrels.")
    printBoard()
    print("This is what the board will look like. Player 1 on the left, and the computer on the right.")
    print("The game will ask for you to hide behind a barrel, and to shoot at an opposing barrel.")
    print("Offscreen the computer will make this same choice.")
    print("The game will announce the draw where it will reveal the choice of both players.")
    print("To win the computer has to be eliminated before Player 1 is eliminated.")
    print("\nHere is how a game would go: ")

    playShootout()
    



def easy():
    print("Welcome to Plano, Texas!\n")
    playShootout()
def medium():
    print("Welcome to Tuscon, Arizona!\n")
    playShootout()
def hard():
    print("Welcome to Las Vegas, Nevada!\n")
    playShootout()

def printBoard():
    if dif == "Tutorial":
        p_board = ["1 |`|", "2 |`|","3 |`|"]
        c_board = ["|`|", "|`|","|`|"]
        for i in range(3):
            print(p_board[i],"\t" ,c_board[i])
            print()
    if dif == "Easy":
        p_board = [" ", "|`|", "|`|","|`|", " "]
        c_board = ["|`|", "|`|","|`|","|`|","|`|"]
        for i in range(5):
            print(p_board[i],"\t" ,c_board[i])
            print()
    if dif == "Medium":
        p_board = [" ", " ", "|`|", "|`|","|`|", " ", " "]
        c_board = ["|`|", "|`|","|`|","|`|","|`|","|`|","|`|"]
        for i in range(7):
            print(p_board[i],"\t" ,c_board[i])
            print()
    if dif == "Hard":
        p_board = [" ", " ", " ", "|`|", "|`|","|`|", " ", " ", " "]
        c_board = ["|`|", "|`|","|`|","|`|","|`|","|`|","|`|","|`|","|`|"]
        for i in range(9):
            print(p_board[i],"\t" ,c_board[i])
            print()
    return p_board, c_board



def playShootout():
    GameOver = False
    if dif == "Tutorial":
        row1 = ["1", "2", "3"]
        p_board = [" |`|", " |`|"," |`|"]
        row2 = ["1", "2", "3"]
        c_board = ["  |`|", "  |`|","  |`|"]
        for i in range(3):
            print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
            print()
    if dif == "Easy":
        row1 = [" ","1", "2", "3", " "]
        p_board = [" ", "|`|", "|`|","|`|", " "]
        row2 = ["1", "2", "3", "4" , "5"]
        c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|"]
        for i in range(5):
            print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
            print()
    if dif == "Medium":
        row1 = [" "," ","1", "2", "3", " ", " "]
        p_board = [" ", " ", "|`|", "|`|","|`|", " ", " "]
        row2 = ["1", "2", "3", "4" , "5", "6", "7"]
        c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
        for i in range(7):
            print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
            print()
    if dif == "Hard":
        row1 = [" "," "," ","1", "2", "3", " ", " "," "]
        p_board = [" ", " ", " ", "|`|", "|`|","|`|", " ", " ", " "]
        row2 = ["1", "2", "3", "4" , "5", "6", "7", "8", "9"]
        c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
        for i in range(9):
            print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
            print()
    
    
    while (GameOver != True):
        if (dif == "Tutorial"):
            i = 1
            j = 0
            k = 3
        elif(dif == "Easy"):
            i = 2
            j = 1
            k = 5
        elif(dif == "Medium"):
            i = 3
            j = 2
            k = 7
        elif(dif == "Hard"):
            i = 4
            j = 3 
            k = 9
        hide = int(input("Player 1, select the barrel you wish to hide behind: "))
        p_board[(hide+j) - 1] = "o|`|"
        
        attack = int(input("Player 1, select the barrel you wish to shoot at: "))
        c_board[attack-1] = "->|`|"
        
        for i in range(k):
            print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
            print()
        print("\nDraw!\n")
        compHide = random.randint(1,k)
        compAttack = random.randint(1,3)
        c_board[compHide-1] = "  |`|o"
        p_board[(compAttack+j) - 1] = "|`|<-"
        if hide == compAttack:
            p_board[(hide+j) - 1] = "o|`|<-"
        elif attack == compHide:
            c_board[compHide-1] = "->|`|o"
        for i in range(k):
            print(row1[i],p_board[i],"\t\t",row2[i],c_board[i])
            print()
        if attack == compHide and hide == compAttack:
            print("\nIt was a tie. Get up and try again!")
        elif attack == compHide:
            print("\nGame Over. You Won!")
            GameOver = True
            break
        elif hide == compAttack:
            print("\nGame Over. You Lost.")
            GameOver = True
            break
        else :
            print("Both players missed. Reload and try and again!")
        if GameOver == False:
            if dif == "Tutorial":
                row1 = ["1", "2", "3"]
                p_board = [" |`|", " |`|"," |`|"]
                row2 = ["1", "2", "3"]
                c_board = ["  |`|", "  |`|","  |`|"]
                for i in range(3):
                    print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
                    print()
            if dif == "Easy":
                row1 = [" ","1", "2", "3", " "]
                p_board = [" ", "|`|", "|`|","|`|", " "]
                row2 = ["1", "2", "3", "4" , "5"]
                c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|"]
                for i in range(5):
                    print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
                    print()
            if dif == "Medium":
                row1 = [" "," ","1", "2", "3", " ", " "]
                p_board = [" ", " ", "|`|", "|`|","|`|", " ", " "]
                row2 = ["1", "2", "3", "4" , "5", "6", "7"]
                c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
                for i in range(7):
                    print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
                    print()
            if dif == "Hard":
                row1 = [" "," "," ","1", "2", "3", " ", " "," "]
                p_board = [" ", " ", " ", "|`|", "|`|","|`|", " ", " ", " "]
                row2 = ["1", "2", "3", "4" , "5", "6", "7", "8", "9"]
                c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
                for i in range(9):
                    print(row1[i],p_board[i],"\t" ,row2[i],c_board[i])
                    print()
        

        



        

        



mapChooser()

dif = input("\nSelect Difficulty: ")

run =  False
while (run != True):
    if (dif == "Tutorial"):
        tutorial()
        run = True
    elif(dif == "Easy"):
        easy()
        run = True
    elif(dif == "Medium"):  
        medium()
        run = True
    elif(dif == "Hard"):
        hard()
        run = True
    else:
        print("Not viable option. Try again")
        dif = input("\nSelect Difficulty: ")



