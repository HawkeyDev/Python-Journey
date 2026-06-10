import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    guess = input("Enter rock, paper, or scissors: ")

    if guess == "rock" and computer == "scissors":
        print("You win!")
    elif  guess == "paper" and computer == "scissors":
        print("You lose!")
    elif guess == "scissors" and computer == "scissors":
        print("Draw")
    elif guess == "rock" and computer == "rock":
        print("Draw")
    elif guess == "paper" and computer == "rock":
        print("You win!")
    elif guess == "scissors" and computer == "rock":
        print("You lose!")
    elif guess == "rock" and computer == "paper":
        print("You lose!")
    elif guess == "paper" and computer == "paper":
        print("Draw!")
    elif guess == "scissors" and computer == "paper":
        print("You win!")
   
    print("Computer choice:", computer)
    play = input("Play again? (yes/no): ")
    if play == "no":
        break