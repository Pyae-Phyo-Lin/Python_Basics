import random

print("\nWelcome from Number Guessing Game.Let's play!\n")

secret_num = random.randint(1, 100)
print("Guess the number! It's between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess number: "))
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        if guess < secret_num:
            print("Too low! Try again.")
        elif guess > secret_num:
            print("Too high! Try again.")
        else:
            print("\nCongratulations! You've guessed the number!\n")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")