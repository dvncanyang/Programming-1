import random

# def all 3 variables
# input player choice
# get random from computer

play_again = "yes"
user_act = input("Enter a choice (rock, paper, scissors): ").lower()
possible_act = ["rock", "paper", "scissors"]
computer_act = random.choice(possible_act)
    
    # check who won
while play_again == "yes":    
    if user_act == computer_act:
        print(f"Both players chose {user_act}. No winners this round!")
    elif user_act == "rock":
        if computer_act == "scissors":
            print("Rock beat scissors! You win!")
        else:
            print("Paper ate rock! You lost..")
    elif user_act == "scissors":
        if computer_act == "rock":
            print("Rock beat scissors! You lost..")
        else:
            print("Paper ate rock! You won!")
    elif user_act == "paper":
        if computer_act == "scissors":
            print("Scissors cut up paper! You lost..")
        else:
            print("Paper ate rock! You won!")
    break
 # play again

play_again = input("Play again? (yes/no): ").lower()