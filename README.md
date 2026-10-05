# Number Guessing Game (Python)

Veda Technology Python Internship — Level 1, Task 5

A game where the program generates a random number and the user keeps guessing until the correct number is found.

## Objective
Learn loops, conditions, random number generation, and user interaction.

## Tools
- Python 3
- `random` module (built in, nothing to install)

## Features
- Picks a random number between 1 and 100 using `random.randint()`
- Tells the user whether each guess is too high or too low
- Counts the number of attempts
- Stops the game as soon as the correct number is guessed
- Invalid input (letters, empty input) does not crash the game and is not counted as an attempt

## How to Run
```bash
python number_guessing_game.py
```

## Approach
- `random.randint(1, 100)` picks the secret number once, before the game starts.
- A `while True` loop keeps asking for guesses until the user is correct.
- `try/except ValueError` around `int(input())` catches non-numeric input and uses `continue` to ask again.
- The attempts counter is increased only after a valid guess.
- An `if / elif / else` compares the guess with the secret number: low, high, or correct. On a correct guess the program prints the attempts and uses `break` to end the loop.

## Sample Gameplay Output

**Game 1: with an invalid input**
```
========================================
       NUMBER GUESSING GAME
========================================
I have picked a number between 1 and 100.
Can you guess it?

Enter your guess: abc
Invalid input! Please enter a whole number.
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 31

Congratulations! You guessed the number 31.
Total attempts: 4
```

**Game 2**
```
========================================
       NUMBER GUESSING GAME
========================================
I have picked a number between 1 and 100.
Can you guess it?

Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 62
Too high! Try again.
Enter your guess: 56
Too low! Try again.
Enter your guess: 59
Too high! Try again.
Enter your guess: 57
Too low! Try again.
Enter your guess: 58

Congratulations! You guessed the number 58.
Total attempts: 7
```

## Interview Questions

**1. What is the random module?**
It is a built-in Python module that generates pseudo-random numbers. `random.randint(a, b)` returns a random whole number between a and b (both included). Other useful functions are `random.choice()`, `random.random()` and `random.shuffle()`.

**2. What is the difference between while and for loops?**
A `for` loop is used when the number of repetitions is known, for example looping over a list or `range(5)`. A `while` loop repeats as long as a condition is true, which is useful when we do not know how many times it will run, like this game where it runs until the user guesses correctly.

**3. How would you limit the number of attempts?**
Set a maximum, for example `max_attempts = 7`, and change the loop to `while attempts < max_attempts:`. If the loop ends without a correct guess, print that the user has lost and show the secret number.

## Outcome
The game works correctly: it gives high/low hints, counts attempts, handles invalid input and ends when the number is guessed.