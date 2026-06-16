import random

input("Press Enter to roll the dice...")
while True:
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}!")
    i = input("Press Enter to roll again or type 'exit' to quit: ")
    if i.lower() == 'exit':
        print("Thanks for playing!")
        break