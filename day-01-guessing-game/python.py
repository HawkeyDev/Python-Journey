import random
number = random.randint(1, 100)

for i in range(7):
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Correct! You got it in", i + 1, "tries")
        break
    elif guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
else:
    print("Game over! The number was:", number)