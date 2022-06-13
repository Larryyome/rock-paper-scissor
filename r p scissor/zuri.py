import random

while True:
    
    choices=["rock", "paper", "scissors"]

    computer=random.choice(choices)
    player=["rock", "paper", "scissors"]

    while player not in choices:
        player= input("rock, paper, scissors: ").lower()

    if player == computer:
        print(computer)
        print(player)
        print("it is a Tie")
    elif player == "rock":
        if computer == "paper":
            print(computer)
            print(player)
            print("you lose")
        if computer == "scissors":
            print(computer)
            print(player)
            print(" wow! you won")
             
        

    elif player == "scissors": #can i use and here
        if computer == "paper":
            print(computer)
            print(player)
            print("you won")
        if computer == "rock":
            print(computer)
            print(player)
            print("you lose")

    elif player == "paper":
        if computer == "rock":
            print(computer)
            print(player)
            print("you won")
        if computer == "scissors":
            print(computer)
            print(player)
            print(" you lose")
    else:
        print("error")
    again= input("do you want to play again? y/n:  ").lower

    if again != "y":
        break