#This is a sample for one line memory game.
#Made by: Mariam Muhammad Yossri
from glob import glob
import random
print("Welcome to one line memory game")
#These are the choices that will appear to the players
choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
#These are the values hidden under the previous choises
values = ["a", "c", "e", "g", "i", "b", "d", "f", "h", "j", "b", "d", "f", "h", "j", "a", "c", "e", "g", "i" ]
random.shuffle(values)
def show():         #define a function called show to print all choices
    print(choices)
def action(player):      #define a function called action to take the action from each player
    global achieved
    global x
    global y
    global actual_x
    global actual_y
    while True:
        x = input("\n" + player + ",Enter your first choice: ")
        y = input("\n" + player + ",Enter your second choice: ")
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if 0<=x<=19 and 0<=y<=19 and x!=y: #to make sure that the chosen numbers are included in the choices
                if choices[x] == "*" or choices[y] == "*" : #to make sure that the chosen choices are not previously guessed
                    print("\n Please enter non previously guessed choices!\n" )
                else:
                    continue
            else:
                print("\nPlease enter two non equal numbers from 0 to 19!\n")
        else:
            print("\nPlease enter two different numbers from 0 to 19!\n")
            continue
    actual_x = choices[x]
    actual_y = choices[y]
    choices[x] = values[x]
    choices[y] = values[y]
    print("\n")
    show()

    if choices[x] == choices[y]: #if choices have equal values displace them by"*"
        choices[x] = "*"
        choices[y] = "*"
        achieved = True
        print(choices, achieved)
    else:
        choices[x] = actual_x
        choices[y] = actual_y
        achieved = False
        print(choices, achieved)

def game_continuity(): #define a function called game_continuity to make sure after each round if the game is continuous or not
    global continuous
    if choices == ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]:
        continuous = False
        return continuous
def play(): #define a function called play starting with zero results for both players
    player1_result = 0
    player2_result = 0
    
    while True:
        show()
        action("Player1")
        if achieved: #if player acheived "guessed right" increase his score by 1 and print the new result
            player1_result += 1
        print("Player1 score is: " + str(player1_result) + "\n")
        game_continuity() #check if game is continous or not after each round
        if not continuous:
            break
        show()
        action("Player2")
        if achieved: #if player acheived "guessed right" increase his score by 1 and print the new result
            player2_result += 1
            print("Player2 score is: " + str(player2_result) == "\n")
            game_continuity() #check if game is continous or not after each round
            if not continuous:
                break
            print("\n")
    if player1_result > player2_result:
        print("Player1 won!")
    else:
        if player2_result > player1_result:
            print("Player2 won!")
        else:
            print("Tie")
play()