import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    guess = input("Enter rock, paper, or scissors: ")

    if guess == computer:
        print("Your choice is right")
    else:
        print("Your guess was wrong")

    print("Computer choice:", computer)
    