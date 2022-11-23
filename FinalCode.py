import random
import re


def mapChooser():
    print("\nWelcome to the Wild West Shootout!")
    
    print("\nTraining Room (Tutorial)")
    print("Plano, Texas (Easy)")
    print("Tuscon, Arizona (Medium)")
    print("Las Vegas, Nevada (Hard)")


def tutorial():
    print("\nWelcome to the Training Range!\n")
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
    print("\nWelcome to Plano, Texas!\n")
    playShootout()
def medium():
    print("\nWelcome to Tuscon, Arizona!\n")
    playShootout()
def hard():
    print("\nWelcome to Las Vegas, Nevada!\n")
    playShootout()

def printBoard():
    if dif == "tutorial":
        p_board = ["1 |`|", "2 |`|","3 |`|"]
        c_board = ["|`|", "|`|","|`|"]
        for i in range(3):
            print(p_board[i],"\t" ,c_board[i])
            print()
    if dif == "easy":
        p_board = [" ", "|`|", "|`|","|`|", " "]
        c_board = ["|`|", "|`|","|`|","|`|","|`|"]
        for i in range(5):
            print(p_board[i],"\t" ,c_board[i])
            print()
    if dif == "medium":
        p_board = [" ", " ", "|`|", "|`|","|`|", " ", " "]
        c_board = ["|`|", "|`|","|`|","|`|","|`|","|`|","|`|"]
        for i in range(7):
            print(p_board[i],"\t" ,c_board[i])
            print()
    if dif == "hard":
        p_board = [" ", " ", " ", "|`|", "|`|","|`|", " ", " ", " "]
        c_board = ["|`|", "|`|","|`|","|`|","|`|","|`|","|`|","|`|","|`|"]
        for i in range(9):
            print(p_board[i],"\t" ,c_board[i])
            print()
    return p_board, c_board



def playShootout():
    GameOver = False
    wins = 0
    losses = 0
    if dif == "tutorial":
        row1 = ["1", "2", "3"]
        p_board = [" |`|", " |`|"," |`|"]
        row2 = ["1", "2", "3"]
        c_board = ["  |`|", "  |`|","  |`|"]
        for i in range(3):
            print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
            print()
    if dif == "easy":
        row1 = [" ","1", "2", "3", " "]
        p_board = [" ", " |`|", " |`|"," |`|", " "]
        row2 = ["1", "2", "3", "4" , "5"]
        c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|"]
        for i in range(5):
            print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
            print()
    if dif == "medium":
        row1 = [" "," ","1", "2", "3", " ", " "]
        p_board = [" ", " ", " |`|", " |`|"," |`|", " ", " "]
        row2 = ["1", "2", "3", "4" , "5", "6", "7"]
        c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
        for i in range(7):
            print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
            print()
    if dif == "hard":
        row1 = [" "," "," ","1", "2", "3", " ", " "," "]
        p_board = [" ", " ", " ", " |`|", " |`|"," |`|", " ", " ", " "]
        row2 = ["1", "2", "3", "4" , "5", "6", "7", "8", "9"]
        c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
        for i in range(9):
            print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
            print()
    
    
    while (GameOver != True):
        if (dif == "tutorial"):
            i = 1
            j = 0
            k = 3
        elif(dif == "easy"):
            i = 2
            j = 1
            k = 5
        elif(dif == "medium"):
            i = 3
            j = 2
            k = 7
        elif(dif == "hard"):
            i = 4
            j = 3 
            k = 9
        hide = int(input("Player 1, select the barrel you wish to hide behind: "))
        while hide > 3 or hide < 1:
            hide = int(input("Please pick a barrel and its respective number: "))
        p_board[(hide+j) - 1] = "o|`|"
        
        attack = int(input("Player 1, select the barrel you wish to shoot at: "))
        while attack > k or attack < 1:
            attack = int(input("Please pick a barrel and its respective number: "))
        c_board[attack-1] = "->|`| "
        
        for i in range(k):
            print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
            print()
        print("\nDraw!\n")
        compHide = random.randint(1,k)
        compAttack = random.randint(1,3)
        c_board[compHide-1] = "  |`|o"
        p_board[(compAttack+j) - 1] = " |`|<-"
        if hide == compAttack:
            p_board[(hide+j) - 1] = "o|`|<-"
        if attack == compHide:
            c_board[compHide-1] = "->|`|o"
        for i in range(k):
            print(row1[i],p_board[i],"\t\t",row2[i],c_board[i])
            print()
        if attack == compHide and hide == compAttack:
            print("\nIt was a tie. Get up and try again!\n")
        elif attack == compHide:
            print("\nGame Over. You Won!")
            GameOver = True
            break
        elif hide == compAttack:
            print("\nGame Over. You Lost.")
            GameOver = True
            break
        else :
            print("Both players missed. Reload and try again!\n")
        if GameOver == False:
            if dif == "tutorial":
                row1 = ["1", "2", "3"]
                p_board = [" |`|", " |`|"," |`|"]
                row2 = ["1", "2", "3"]
                c_board = ["  |`|", "  |`|","  |`|"]
                for i in range(3):
                    print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
                    print()
            if dif == "easy":
                row1 = [" ","1", "2", "3", " "]
                p_board = [" ", " |`|", " |`|"," |`|", " "]
                row2 = ["1", "2", "3", "4" , "5"]
                c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|"]
                for i in range(5):
                    print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
                    print()
            if dif == "medium":
                row1 = [" "," ","1", "2", "3", " ", " "]
                p_board = [" ", " ", " |`|", " |`|"," |`|", " ", " "]
                row2 = ["1", "2", "3", "4" , "5", "6", "7"]
                c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
                for i in range(7):
                    print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
                    print()
            if dif == "hard":
                row1 = [" "," "," ","1", "2", "3", " ", " "," "]
                p_board = [" ", " ", " ", " |`|", " |`|"," |`|", " ", " ", " "]
                row2 = ["1", "2", "3", "4" , "5", "6", "7", "8", "9"]
                c_board = ["  |`|", "  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|","  |`|"]
                for i in range(9):
                    print(row1[i],p_board[i],"\t\t" ,row2[i],c_board[i])
                    print()
        

def playAgain():
    print("\nDo you wish to play again? ") 
    playAgain = input("Yes or No? ") 
    playerChoice = playAgain.lower()
    while playerChoice != "yes" or playerChoice != "no":
        if playerChoice == "yes":
            break
        elif playerChoice == "no":
            break
        print("Please select a viable option")
        print("\nDo you wish to play again? ") 
        playAgain = input("Yes or No? ") 
        playerChoice = playAgain.lower()
    if playerChoice == "yes":
        return True
    elif playerChoice == "no":
        return False


#to remind taylor later, add game over and add regex to difficulty and game over 



mapChooser()

dif = input("\nSelect Difficulty: ")
dif = dif.lower()

exit =  False
while (exit != True):
    if (dif == "tutorial"):
        tutorial()
        again = playAgain()
        if again == False:
            exit = True
            break
        if again == True:
            mapChooser()
            dif = input("\nSelect Difficulty: ")
            dif = dif.lower()
    elif(dif == "easy"):
        easy()
        again = playAgain()
        if again == False:
            exit = True
            break
        if again == True:
            mapChooser()
            dif = input("\nSelect Difficulty: ")
            dif = dif.lower()
    elif(dif == "medium"):  
        medium()
        again = playAgain()
        if again == False:
            exit = True
            break
        if again == True:
            mapChooser()
            dif = input("\nSelect Difficulty: ")
            dif = dif.lower()
    elif(dif == "hard"):
        hard()
        again = playAgain()
        if again == False:
            exit = True
            break
        if again == True:
            mapChooser()
            dif = input("\nSelect Difficulty: ")
            dif = dif.lower()
    else:
        print("Not viable option. Try again")
        dif = input("\nSelect Difficulty: ")



