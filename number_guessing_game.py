# Veda Technology - Task 5 
# Number Guessing Game

import random

secret_number = random.randint(1, 100)
attempts = 0

print("=" * 40)
print("       NUMBER GUESSING GAME")
print("=" * 40)
print("I have picked a number between 1 and 100.")
print("Can you guess it?\n")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"\nCongratulations! You guessed the number {secret_number}.")
        print(f"Total attempts: {attempts}")
        break
