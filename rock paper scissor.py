#Import random module 
import random 
 
#Create a list of play options 
play = ["Rock", "Paper", "Scissors"]

#Assign a random play to the system 
computer = play[random.randint(0,2)] 
 
#Set the player to False 
player = False

while player == False: 
#Set the player to True 
    player = input("Rock, Paper, Scissors?") 
    if player == computer: 
        print("Tie!") 
    elif player == "Rock": 
        if computer == "Paper": 
            print("You lose!", computer, "covers", player) 
        else: 
            print("You win!", player, "smashes", computer) 
    elif player == "Paper": 
        if computer == "Scissors": 
            print("You lose!", computer, "cuts", player) 
        else: 
            print("You win!", player, "covers", computer) 
    elif player == "Scissors": 
        if computer == "Rock": 
            print("You lose...", computer, "smashes", player) 
        else: 
            print("You win!", player, "cuts", computer) 
    else: 
        print("That's not a valid play. Check the spelling!") 
    #Player was set to True, but we want it to be False so the loop continues 
    player = False 
    computer = play[random.randint(0,2)]
